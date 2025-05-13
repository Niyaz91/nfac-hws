from pydantic import BaseModel, EmailStr

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
