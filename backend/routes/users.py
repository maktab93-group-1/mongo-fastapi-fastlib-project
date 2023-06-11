from fastapi import APIRouter, Depends, HTTPException
from schemas.users import CreateUser, ReturnUser
from schemas.tokens import Token
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from auth.jwt_utils import get_access_token
from crud.users import create_user
from db import USERS
from auth.auth_utils import get_password_hash

user_router = APIRouter(prefix="/users", tags=["users"])

@user_router.post("/register/",response_model=ReturnUser)
def register(user: CreateUser): 
    user = user.dict()
    in_db_user = CreateUser(password=get_password_hash(user.pop('password')), **user)
    result = create_user(USERS,in_db_user)
    if not result:
        raise HTTPException(status_code=422, detail="Could not create user!")
    return user

@user_router.post("/login/",response_model=Token)
def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    access_token = get_access_token(form_data)
    return {"access_token": access_token, "token_type": "bearer"}