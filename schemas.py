from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: EmailStr
    phone: str
    password: str
    name: str
    city: str

class UserOut(BaseModel):
    id: int
    username: EmailStr
    phone: str
    name: str
    city: str

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    phone: Optional[str] = None
    name: Optional[str] = None
    city: Optional[str] = None

class ShanyrakCreate(BaseModel):
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: Optional[str] = None

class ShanyrakOut(BaseModel):
    id: int

    class Config:
        orm_mode = True

class ShanyrakDetail(BaseModel):
    id: int
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: Optional[str]
    user_id: int
    total_comments: int

    class Config:
        orm_mode = True

class ShanyrakUpdate(BaseModel):
    type: Optional[str]
    price: Optional[int]
    address: Optional[str]
    area: Optional[float]
    rooms_count: Optional[int]
    description: Optional[str]

class CommentCreate(BaseModel):
    content: str

class CommentOut(BaseModel):
    id: int
    content: str
    created_at: datetime
    user_id: int
    shanyrak_id: int

    class Config:
        orm_mode = True

class CommentListItem(BaseModel):
    id: int
    content: str
    created_at: datetime
    author_id: int  # отображаем как author_id, хотя в модели это user_id

    class Config:
        orm_mode = True

class CommentList(BaseModel):
    comments: list[CommentListItem]

class CommentUpdate(BaseModel):
    content: str


