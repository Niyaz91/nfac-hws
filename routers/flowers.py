from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import models
from schemas import schemas

router = APIRouter()

@router.get("/flowers", response_model=List[schemas.FlowerOut])
def get_flowers(db: Session = Depends(get_db)):
    return db.query(models.Flower).all()

@router.post("/flowers", response_model=schemas.FlowerOut)
def create_flower(flower: schemas.FlowerCreate, db: Session = Depends(get_db)):
    db_flower = models.Flower(**flower.dict())
    db.add(db_flower)
    db.commit()
    db.refresh(db_flower)
    return db_flower

@router.patch("/flowers/{flower_id}")
def update_flower(flower_id: int, flower: schemas.FlowerCreate, db: Session = Depends(get_db)):
    db_flower = db.query(models.Flower).filter_by(id=flower_id).first()
    if not db_flower:
        raise HTTPException(status_code=404)
    for key, value in flower.dict().items():
        setattr(db_flower, key, value)
    db.commit()
    return db_flower

@router.delete("/flowers/{flower_id}")
def delete_flower(flower_id: int, db: Session = Depends(get_db)):
    db_flower = db.query(models.Flower).filter_by(id=flower_id).first()
    if not db_flower:
        raise HTTPException(status_code=404)
    db.delete(db_flower)
    db.commit()
    return {"ok": True}
