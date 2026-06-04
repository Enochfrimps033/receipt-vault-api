from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.user_schema import UserCreate, UserLogin, UserResponse, TokenResponse
from viewmodels.auth_viewmodel import AuthViewModel

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register, response_model=UserResponse")
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    auth_vm=AuthViewModel(db)
    return auth_vm.register_user(user_data)