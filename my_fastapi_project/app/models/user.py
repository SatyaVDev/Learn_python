# app/models/user.py
from sqlalchemy import Column, Integer, String
# from app.database.db import Base  # Import Base from db.py
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"  # Name of the table in the database

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
