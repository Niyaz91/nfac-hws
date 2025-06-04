from fastapi import FastAPI, Request, Form, Depends, Response, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from app.utils import hash_password, verify_password
from jose import jwt
from app.config import SECRET_KEY, ALGORITHM
from app.models.task import Task
from fastapi import Form
from app.models.project import Project
from jose import JWTError
from datetime import datetime
from fastapi import Query
from fastapi.responses import HTMLResponse
from app.models.user_project import UserProject, RoleEnum
from app.dependencies import get_current_user
from app.routes import task

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def welcome(request: Request):
    return templates.TemplateResponse("welcome.html", {"request": request})

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/register")
def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
def register_user(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    if db.query(User).filter(User.username == username).first():
        return templates.TemplateResponse("register.html", {"request": request, "error": "Username already taken"})

    user = User(username=username, email=email, hashed_password=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return RedirectResponse("/login", status_code=302)

@app.get("/login")
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def login_user(
    response: Response,
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})

    token = jwt.encode({"sub": user.username}, SECRET_KEY, algorithm=ALGORITHM)
    response = RedirectResponse("/projects", status_code=302)
    response.set_cookie("access_token", token, httponly=True)
    return response

@app.get("/projects")
def show_projects(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    if not token:
        return RedirectResponse("/login", status_code=302)

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
    except JWTError:
        return RedirectResponse("/login", status_code=302)

    user = db.query(User).filter(User.username == username).first()
    if not user:
        return RedirectResponse("/login", status_code=302)

    projects = (
        db.query(Project)
        .join(UserProject)
        .filter(UserProject.user_id == user.id)  # <= Заменил current_user на user
        .all()
    )
    return templates.TemplateResponse("projects.html", {"request": request, "projects": projects})


@app.get("/logout")
def logout():
    response = RedirectResponse("/login", status_code=302)
    response.delete_cookie("access_token")
    return response


@app.get("/projects/create")
def create_project_form(
    request: Request,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    users = db.query(User).filter(User.id != current_user.id).all()
    return templates.TemplateResponse("create_project.html", {
        "request": request,
        "users": users
    })

@app.post("/projects/create")
def create_project(
    request: Request,
    name: str = Form(...),
    description: str = Form(""),
    deadline: str = Form(""),
    members: list[int] = Form(default=[]),
    db: Session = Depends(get_db)
):
    token = request.cookies.get("access_token")
    if not token:
        return RedirectResponse("/login", status_code=302)

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
    except JWTError:
        return RedirectResponse("/login", status_code=302)

    user = db.query(User).filter(User.username == username).first()
    if not user:
        return RedirectResponse("/login", status_code=302)

    # Обработка дедлайна
    deadline_dt = datetime.strptime(deadline, "%Y-%m-%d").date() if deadline else None

    # Создание проекта
    new_project = Project(
        name=name,
        description=description,
        owner_id=user.id,
        deadline=deadline_dt
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    # Добавить владельца как участника (OWNER)
    db.add(UserProject(user_id=user.id, project_id=new_project.id, role=RoleEnum.OWNER))

    # Добавить остальных участников, исключая владельца
    unique_members = set(members)
    if user.id in unique_members:
        unique_members.remove(user.id)

    for member_id in unique_members:
        db.add(UserProject(user_id=member_id, project_id=new_project.id, role=RoleEnum.MEMBER))

    db.commit()

    return RedirectResponse("/projects", status_code=302)


@app.get("/projects/{project_id}")
def view_project(request: Request, project_id: int, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    if not token:
        return RedirectResponse("/login", status_code=302)

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
    except JWTError:
        return RedirectResponse("/login", status_code=302)

    user = db.query(User).filter(User.username == username).first()
    if not user:
        return RedirectResponse("/login", status_code=302)

    project = (
        db.query(Project)
        .join(UserProject)
        .filter(Project.id == project_id, UserProject.user_id == user.id)
        .first()
    )
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    tasks = db.query(Task).filter(Task.project_id == project.id).all()
    members = db.query(UserProject).filter(UserProject.project_id == project.id).all()

    is_owner = project.owner_id == user.id

    return templates.TemplateResponse("project_detail.html", {
        "request": request,
        "project": project,
        "tasks": tasks,
        "members": members,
        "owner": project.owner,
        "is_owner": is_owner
    })


@app.get("/projects/{project_id}/edit")
def edit_project_form(project_id: int, request: Request, db: Session = Depends(get_db),
                      user: User = Depends(get_current_user)):
    project = db.query(Project).get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    users = db.query(User).all()
    current_member_ids = [link.user_id for link in project.user_links]

    return templates.TemplateResponse("edit_project.html", {
        "request": request,
        "project": project,
        "users": users,
        "current_member_ids": current_member_ids
    })

@app.post("/projects/{project_id}/edit")
def edit_project(
    project_id: int,
    name: str = Form(...),
    description: str = Form(""),
    deadline: str = Form(""),
    members: list[int] = Form(default=[]),
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    project.name = name
    project.description = description
    project.deadline = datetime.strptime(deadline, "%Y-%m-%d") if deadline else None

    # Удалить старых участников, кроме owner
    db.query(UserProject).filter(
        UserProject.project_id == project_id,
        UserProject.user_id != project.owner_id
    ).delete()

    # Добавить новых участников, кроме owner
    for member_id in members:
        if member_id != project.owner_id:
            db.add(UserProject(user_id=member_id, project_id=project_id, role="MEMBER"))

    db.commit()
    return RedirectResponse(f"/projects/{project_id}", status_code=302)

@app.get("/projects/{project_id}/delete")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(project)
    db.commit()
    return RedirectResponse("/projects", status_code=302)

from app.routes.task import router as task_router
app.include_router(task_router)

@app.post("/projects/{project_id}/edit")
def edit_project(
    project_id: int,
    name: str = Form(...),
    description: str = Form(...),
    deadline: str = Form(...),
    member_usernames: list[str] = Form(default=[]),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    project.name = name
    project.description = description
    project.deadline = deadline

    # Обновим участников
    existing_links = {link.user.username: link for link in project.user_links if link.role.name == "MEMBER"}

    for username in member_usernames:
        if username not in existing_links:
            user = db.query(User).filter_by(username=username).first()
            if user:
                project.user_links.append(UserProject(user=user, role=RoleEnum.MEMBER))

    db.commit()
    return RedirectResponse(f"/projects/{project_id}", status_code=302)


@app.get("/projects/{project_id}/tasks/{task_id}/edit")
def edit_task_form(project_id: int, task_id: int, request: Request, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.project_id == project_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return templates.TemplateResponse("edit_task.html", {"request": request, "task": task, "project_id": project_id})

@app.post("/projects/{project_id}/tasks/{task_id}/edit")
def update_task(
    project_id: int,
    task_id: int,
    title: str = Form(...),
    description: str = Form(""),
    status: str = Form(...),
    priority: int = Form(0),
    deadline: str = Form(""),
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    task = db.query(Task).filter(Task.id == task_id, Task.project_id == project_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = title
    task.description = description
    task.status = status
    task.priority = priority
    task.deadline_dt = datetime.strptime(deadline, "%Y-%m-%d").date() if deadline else None

    db.commit()
    return RedirectResponse(f"/projects/{project_id}", status_code=302)

@app.get("/projects/{project_id}/tasks/{task_id}/delete")
def delete_task(project_id: int, task_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.project_id == project_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return RedirectResponse(f"/projects/{project_id}", status_code=302)

@app.post("/projects/{project_id}/status")
def update_project_status(
    project_id: int,
    status: str = Form(...),
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # только owner может менять статус
    if project.owner_id != user.id:
        raise HTTPException(status_code=403, detail="You are not the owner")

    project.status = status
    db.commit()
    return RedirectResponse(f"/projects/{project_id}", status_code=302)

@app.post("/projects/{project_id}/tasks")
def create_task_for_project(
    request: Request,
    project_id: int,
    title: str = Form(...),
    description: str = Form(None),
    status: str = Form(...),
    priority: int = Form(None),
    deadline: str = Form(None),
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    # Проверка существования проекта
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # Проверка: пользователь должен быть участником проекта
    link = db.query(UserProject).filter_by(user_id=user.id, project_id=project.id).first()
    if not link:
        raise HTTPException(status_code=403, detail="You are not a member of this project")

    # Обработка даты
    deadline_dt = None
    if deadline:
        try:
            deadline_dt = datetime.strptime(deadline, "%Y-%m-%d")
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid deadline format")

    # Создание задачи
    new_task = Task(
        title=title,
        description=description,
        status=status,
        priority=priority,
        deadline=deadline_dt,
        project_id=project.id,
    )
    db.add(new_task)
    db.commit()

    return RedirectResponse(url=f"/projects/{project_id}", status_code=302)