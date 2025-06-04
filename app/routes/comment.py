from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import comment as models
from app.schemas import comment as schemas

router = APIRouter(prefix="/comments", tags=["Comments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.CommentResponse)
def add_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    db_comment = models.Comment(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

@router.get("/task/{task_id}", response_model=list[schemas.CommentResponse])
def get_comments_for_task(task_id: int, db: Session = Depends(get_db)):
    return db.query(models.Comment).filter(models.Comment.task_id == task_id).all()
