from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import UserCreate, UserOut
from crud.user import create_user
from database import get_db

router = APIRouter(prefix="/auth/users", tags=["auth"])

@router.post("/", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)
