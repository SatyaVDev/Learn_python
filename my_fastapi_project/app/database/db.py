# app/database/db.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base  # Correct import
from sqlalchemy.orm import sessionmaker
from app.settings.config import settings  # Import settings

# Use DATABASE_URL from the settings (either from .env or default)
DATABASE_URL = settings.DATABASE_URL

# SQLAlchemy Database Engine
engine = create_engine(DATABASE_URL)

# SQLAlchemy Session Local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base for SQLAlchemy Models
Base = declarative_base()  # This is where declarative_base is used

async def get_db():
    """Returns a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
