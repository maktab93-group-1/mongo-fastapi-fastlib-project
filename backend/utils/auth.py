from datetime import timedelta, datetime
from fastapi import FastAPI, HTTPException, Depends
from passlib.context import CryptContext
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, OAuth2AuthorizationCodeBearer, OAuth2PasswordBearer
from jose import JWTError, jwt
from dotenv import load_dotenv
import os

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Load Environment Variables
load_dotenv()



# Extract env vars
ALGORITHM = os.environ['ALGORITHM']
SECRET_KEY = os.environ['SECRET_KEY']
