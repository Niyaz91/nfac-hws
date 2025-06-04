from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum



class RoleEnum(str, enum.Enum):
    OWNER = "owner"
    MEMBER = "member"

class UserProject(Base):
    __tablename__ = "user_project"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), primary_key=True)
    role = Column(Enum(RoleEnum), nullable=False)

    user = relationship("User", back_populates="user_links")
    project = relationship("Project", back_populates="user_links")
