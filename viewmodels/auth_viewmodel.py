from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from models.user_model import User
from schemas.user_schema import UserCreate, UserLogin
from auth import hash_password, verify_password, 


class AuthViewModel:
    def __init__(self, db:Session):
        self.db = db

    def register_user(self, user_data: UserCreate):
        existing_user = (
            self.db.query(User)
            .filter(User.email == user_data.email)
            .first()
        )

        if existing_user:
            raise HTTPException(
                status_code = staus.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            
            )

        new_user = User(
            email = user_data.email,
            hash_password = hash_password(user_data.password)
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        return new_user

    def login_user(self, login_data: UserLogin):
        user = (
            self.db.query(User)
            .filter(User.email == login_data.email)
            .first()
        )

        if not user:
             raise HTTPException(
                status_code = staus.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            
            )
        if not verify_password(login_data.password,user.hashed_password):
            raise HTTPException(
                 status_code = staus.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            
            )

            access_token = create_access_token(
                data = {"sub": user.email}
            )

            return{ "access_token": access_token,
             "token_type": "bearer"
            }