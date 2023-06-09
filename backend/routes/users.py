from fastapi import APIRouter, Depends, HTTPException
from schemas.users import CreateUser, ReturnUser
from schemas.tokens import Token
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from auth.jwt_utils import get_access_token
from crud.users import create_user
from db import USERS


user_router = APIRouter(prefix="/users")

@user_router.post("/register/",response_model=ReturnUser)
def register(user: CreateUser): # TODO check if the user exists
    result = create_user(USERS,user)
    if not result:
        raise HTTPException(status_code=422, detail="Could not create user!")
    return user

@user_router.post("/login/",response_model=Token)
def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    access_token = get_access_token(form_data)
    return {"access_token": access_token, "token_type": "bearer"}