from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import user_project as models
from app.models import project as project_model, user as user_model
from app.schemas import user_project as schemas

router = APIRouter(prefix="/team", tags=["Team"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/add-user/{project_id}")
def add_user_to_project(
    project_id: int,
    data: schemas.AddUserToProject,
    db: Session = Depends(get_db)
):
    # проверим, существует ли проект
    project = db.query(project_model.Project).get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # проверим, существует ли пользователь
    user = db.query(user_model.User).get(data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # добавим пользователя
    association = models.UserProject(
        user_id=data.user_id,
        project_id=project_id,
        role=data.role
    )
    db.add(association)
    db.commit()
    return {"ok": True}
