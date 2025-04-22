from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    type: str = "bearer"

class Flower(BaseModel):
    id: int
    name: str
    price: float
