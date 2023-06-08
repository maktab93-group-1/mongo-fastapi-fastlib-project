from pydantic import BaseModel
from bson import objectId


class CreateUser(BaseModel):
    username: str | None = None
    hashed_password: str | None = None
    is_active: bool | None = True
    
class ReturnUser(BaseModel):
    _id : objectId | None = None
    username: str | None = None