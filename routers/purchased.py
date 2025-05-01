from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import models
from schemas import schemas

router = APIRouter()

@router.post("/purchased", response_model=schemas.PurchaseOut)
def purchase_flower(purchase: schemas.PurchaseCreate, db: Session = Depends(get_db)):
    db_purchase = models.Purchase(user_id=purchase.user_id, flower_id=purchase.flower_id)
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase

@router.get("/purchased", response_model=List[schemas.PurchaseOut])
def get_purchases(db: Session = Depends(get_db)):
    return db.query(models.Purchase).all()
