from pydantic import BaseModel
from enum import Enum

class RoleEnum(str, Enum):
    owner = "owner"
    member = "member"

class AddUserToProject(BaseModel):
    user_id: int
    role: RoleEnum = RoleEnum.member
