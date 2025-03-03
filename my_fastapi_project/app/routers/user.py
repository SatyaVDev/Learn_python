from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session  # Import SQLAlchemy session
from app.database.db import get_db  # Import get_db from db.py
from app import models
from app.services import get_users

router = APIRouter()

@router.get("/", )
async def read_user(user: int, db: Session = Depends(get_db)):
   return  get_users(db)