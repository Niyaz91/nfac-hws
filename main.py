from fastapi import FastAPI, HTTPException, Depends, Form, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Shanyrak, Comment
from schemas import UserCreate, UserOut, UserUpdate, ShanyrakCreate, ShanyrakOut, ShanyrakDetail, ShanyrakUpdate, CommentCreate, CommentOut, CommentListItem, CommentList, CommentUpdate
from auth import create_access_token, get_current_user
from database import get_db, engine


DATABASE_URL = "sqlite:///./test.db"


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.post("/auth/users/", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already registered")

    new_user = User(
        username=user.username,
        phone=user.phone,
        password=user.password,  # ⛔ пароль сохраняется в открытом виде
        name=user.name,
        city=user.city
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.post("/auth/users/login")
def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token_data = {"sub": user.username}
    access_token = create_access_token(data=token_data)
    return JSONResponse(content={"access_token": access_token}, status_code=200)


@app.patch("/auth/users/me", response_model=UserOut)
def update_user_me(update: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if update.phone:
        current_user.phone = update.phone
    if update.name:
        current_user.name = update.name
    if update.city:
        current_user.city = update.city

    db.commit()
    db.refresh(current_user)
    return current_user


@app.get("/auth/users/me", response_model=UserOut)
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user


@app.post("/shanyraks/", response_model=ShanyrakOut)
def create_shanyrak(
    shanyrak: ShanyrakCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_item = Shanyrak(
        user_id=current_user.id,
        type=shanyrak.type,
        price=shanyrak.price,
        address=shanyrak.address,
        area=shanyrak.area,
        rooms_count=shanyrak.rooms_count,
        description=shanyrak.description
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return {"id": new_item.id}


@app.get("/shanyraks/{id}", response_model=ShanyrakDetail)
def get_shanyrak(id: int, db: Session = Depends(get_db)):
    shanyrak = db.query(Shanyrak).filter(Shanyrak.id == id).first()
    if not shanyrak:
        raise HTTPException(status_code=404, detail="Shanyrak not found")

    comment_count = db.query(Comment).filter(Comment.shanyrak_id == id).count()

    return {
        "id": shanyrak.id,
        "type": shanyrak.type,
        "price": shanyrak.price,
        "address": shanyrak.address,
        "area": shanyrak.area,
        "rooms_count": shanyrak.rooms_count,
        "description": shanyrak.description,
        "user_id": shanyrak.user_id,
        "total_comments": comment_count  # 👈 обязательно включи это поле
    }


@app.patch("/shanyraks/{id}")
def update_shanyrak(
    id: int,
    updates: ShanyrakUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    shanyrak = db.query(Shanyrak).filter(Shanyrak.id == id).first()

    if not shanyrak:
        raise HTTPException(status_code=404, detail="Shanyrak not found")

    if shanyrak.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this listing")

    for field, value in updates.dict(exclude_unset=True).items():
        setattr(shanyrak, field, value)

    db.commit()
    return {"message": "Shanyrak updated successfully"}


@app.delete("/shanyraks/{id}")
def delete_shanyrak(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    shanyrak = db.query(Shanyrak).filter(Shanyrak.id == id).first()

    if not shanyrak:
        raise HTTPException(status_code=404, detail="Shanyrak not found")

    if shanyrak.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this listing")

    db.delete(shanyrak)
    db.commit()
    return {"message": "Shanyrak deleted successfully"}


@app.post("/shanyraks/{id}/comments", response_model=CommentOut)
def add_comment(
    id: int,
    comment: CommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    shanyrak = db.query(Shanyrak).filter(Shanyrak.id == id).first()
    if not shanyrak:
        raise HTTPException(status_code=404, detail="Shanyrak not found")

    new_comment = Comment(
        content=comment.content,
        user_id=current_user.id,
        shanyrak_id=id
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


@app.get("/shanyraks/{id}/comments", response_model=CommentList)
def get_comments(id: int, db: Session = Depends(get_db)):
    shanyrak = db.query(Shanyrak).filter(Shanyrak.id == id).first()
    if not shanyrak:
        raise HTTPException(status_code=404, detail="Shanyrak not found")

    comments = db.query(Comment).filter(Comment.shanyrak_id == id).order_by(Comment.created_at.desc()).all()

    # Переименуем user_id в author_id для соответствия требованию
    result = [
        CommentListItem(
            id=c.id,
            content=c.content,
            created_at=c.created_at,
            author_id=c.user_id
        ) for c in comments
    ]

    return {"comments": result}


@app.patch("/shanyraks/{id}/comments/{comment_id}")
def update_comment(
    id: int,
    comment_id: int,
    updated: CommentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Проверяем, что объявление существует
    shanyrak = db.query(Shanyrak).filter(Shanyrak.id == id).first()
    if not shanyrak:
        raise HTTPException(status_code=404, detail="Shanyrak not found")

    # Проверяем, что комментарий существует и принадлежит текущему пользователю
    comment = db.query(Comment).filter(Comment.id == comment_id, Comment.shanyrak_id == id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    if comment.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this comment")

    comment.content = updated.content
    db.commit()
    db.refresh(comment)
    return {"message": "Comment updated successfully"}


@app.delete("/shanyraks/{id}/comments/{comment_id}")
def delete_comment(
    id: int,
    comment_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Проверка наличия объявления
    shanyrak = db.query(Shanyrak).filter(Shanyrak.id == id).first()
    if not shanyrak:
        raise HTTPException(status_code=404, detail="Shanyrak not found")

    # Проверка комментария
    comment = db.query(Comment).filter(Comment.id == comment_id, Comment.shanyrak_id == id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    if comment.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this comment")

    db.delete(comment)
    db.commit()
    return {"message": "Comment deleted successfully"}


