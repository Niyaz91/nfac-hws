from pydantic import BaseModel
from datetime import datetime

class CommentCreate(BaseModel):
    content: str
    task_id: int
    user_id: int

class CommentResponse(CommentCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
