from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

class Flower(Base):
    __tablename__ = "flowers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)

class Purchase(Base):
    __tablename__ = "purchases"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    flower_id = Column(Integer, ForeignKey("flowers.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
