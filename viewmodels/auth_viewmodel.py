from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from models.user_model import User
from schemas.user_schema import UserCreate, UserLogin
from auth import hash_password, verify_password, create_access_token