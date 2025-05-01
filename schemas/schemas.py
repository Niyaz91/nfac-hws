from pydantic import BaseModel
from datetime import datetime
from typing import List

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

class FlowerCreate(BaseModel):
    name: str
    price: int

class FlowerOut(FlowerCreate):
    id: int
    class Config:
        orm_mode = True

class PurchaseCreate(BaseModel):
    user_id: int
    flower_id: int

class PurchaseOut(BaseModel):
    id: int
    user_id: int
    flower_id: int
    timestamp: datetime
    class Config:
        orm_mode = True
