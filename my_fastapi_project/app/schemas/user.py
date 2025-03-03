# app/schemas/user.py
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True  # This tells Pydantic to treat the SQLAlchemy model as a dict
