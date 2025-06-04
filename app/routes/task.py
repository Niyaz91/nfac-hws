from fastapi import APIRouter, Depends, HTTPException, Query, Form
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from app.database import SessionLocal
from app.models import task as models
from app.schemas import task as schemas
from app.models import Task, Project, UserProject, User
from app.dependencies import get_current_user
from fastapi.responses import RedirectResponse

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/projects/{project_id}/tasks")
def create_task_for_project(
    project_id: int,
    title: str = Form(...),
    description: str = Form(None),
    status: str = Form(...),
    priority: int = Form(None),
    deadline: str = Form(None),
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    # Проверка: существует ли проект
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # Проверка: является ли пользователь участником проекта (OWNER или MEMBER)
    link = db.query(UserProject).filter_by(project_id=project_id, user_id=user.id).first()
    if not link:
        raise HTTPException(status_code=403, detail="You are not a member of this project")

    # Создание задачи
    new_task = Task(
        title=title,
        description=description,
        status=status,
        priority=priority,
        deadline=deadline,
        project_id=project_id,
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return RedirectResponse(url=f"/projects/{project_id}", status_code=302)

@router.get("/", response_model=list[schemas.TaskResponse])
def list_tasks(
    db: Session = Depends(get_db),
    sort_by: str = Query("priority", enum=["priority", "deadline"]),
    order: str = Query("asc", enum=["asc", "desc"])
):
    query = db.query(models.Task)
    column = getattr(models.Task, sort_by)
    query = query.order_by(asc(column)) if order == "asc" else query.order_by(desc(column))
    return query.all()

@router.put("/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).get(task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in task.dict().items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).get(task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return {"ok": True}
