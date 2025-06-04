from pydantic import BaseModel
from datetime import datetime
from typing import Literal


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    priority: int = 0
    deadline: datetime | None = None
    status: Literal["todo", "in_progress", "done"] = "todo"
    project_id: int

class TaskResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True
