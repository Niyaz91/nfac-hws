from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship, declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    email = Column(String, unique=True)

    purchases = relationship("Purchase", back_populates="user")

class Flower(Base):
    __tablename__ = 'flowers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    description = Column(String)

    purchases = relationship("Purchase", back_populates="flower")

class Purchase(Base):
    __tablename__ = 'purchases'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    flower_id = Column(Integer, ForeignKey('flowers.id'))
    quantity = Column(Integer)
    purchased_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="purchases")
    flower = relationship("Flower", back_populates="purchases")
