# app/settings/config.py
import os
from dotenv import load_dotenv
from pydantic import BaseModel

# Load the .env file
load_dotenv()  # Automatically loads environment variables from .env

class Settings(BaseModel):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:Admin@localhost:5432/face_database")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "mysecretkey")
    DEBUG: bool = os.getenv("DEBUG", False)
    API_KEY: str = os.getenv("API_KEY", "defaultapikey")
# Instantiate the settings class
settings = Settings()
