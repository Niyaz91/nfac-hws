from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_user(db: Session, user: UserCreate):
    db_user = User(
        username=user.username,
        phone=user.phone,
        password_hash=get_password_hash(user.password),
        name=user.name,
        city=user.city
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
