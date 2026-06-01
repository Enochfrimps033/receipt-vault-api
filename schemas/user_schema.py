from pydantic import BaseMode, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email:EmailStr
    password: str

class UserLogin(BaseModel):
    email:EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
     email:EmailStr
     created_at: datetime

     class config:
        from_attributes = True