from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    user_links = relationship("UserProject", back_populates="user", cascade="all, delete-orphan", passive_deletes=True)
    projects = association_proxy("user_links", "project")

