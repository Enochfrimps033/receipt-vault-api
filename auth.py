import os
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv
from jose import JWTError, jwt
from passlib.context import CryptContext

load_dotenv(dotenv_path=".env")

SECRET_KEY = os.getenv("SECRET_KEY")
# print("SECRET_KEY LOADED:", SECRET_KEY)

ALGORITHM = "HS256"#Use the "HS256 sigining algo for JWT tokens
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password:str):
    return pwd_context.verify(plain_password,hashed_password)

def create_access_token(data: dict):
    copy_of_the_data = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    copy_of_the_data.update({"exp":expire})

    access_token = jwt.encode(copy_of_the_data, SECRET_KEY, algorithm=ALGORITHM)

    return access_token