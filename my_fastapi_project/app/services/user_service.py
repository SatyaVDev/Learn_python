# app/services/user_service.py

from sqlalchemy.orm import Session
from app.models import user as models  # Assuming the User model is in the app.models module
from fastapi import HTTPException


def get_users(db: Session):
    """
    Fetch all users from the database.

    :param db: Database session
    :return: List of users
    """
    db_users = db.query(models.User).all()
    if not db_users:  # If the result is empty, raise an HTTP exception
        raise HTTPException(status_code=404, detail="Users not found")
    return db_users
