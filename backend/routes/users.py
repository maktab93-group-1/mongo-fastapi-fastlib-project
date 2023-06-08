from fastapi import APIRouter
from schemas.users import *


user_router = APIRouter(prefix="/users")

@user_router.post("/register/",response_model=ReturnUser)
def register(User: CreateUser):
    pass

@user_router.post("/login/",response_model=ReturnUser)
def login(User: CreateUser):
    pass

