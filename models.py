from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=False)
    password = Column(String, nullable=False)  # ⚠️ Здесь теперь хранится открытый пароль
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)

class Shanyrak(Base):
    __tablename__ = "shanyraks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    type = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    area = Column(Float, nullable=False)
    rooms_count = Column(Integer, nullable=False)
    description = Column(String, nullable=True)

    owner = relationship("User", backref="shanyraks")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    shanyrak_id = Column(Integer, ForeignKey("shanyraks.id"), nullable=False)

    user = relationship("User", backref="comments")
    shanyrak = relationship("Shanyrak", backref="comments")