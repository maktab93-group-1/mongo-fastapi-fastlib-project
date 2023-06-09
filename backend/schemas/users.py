from pydantic import BaseModel , EmailStr
# from bson import objectId



# class CustomBaseModel(BaseModel):
#     _collection_name : str | None = None
    
#     @property
#     def collection_name(self):
#         return self._collection_name
    

# class BaseUserModel(CustomBaseModel):
#     _collection_name = 'USERS'

class CreateUser(BaseModel):
    username: str | None = None
    password: str | None = None
    email: EmailStr | None = None
    is_active: bool | None = True
    
class ReturnUser(BaseModel):
    _id : str | None = None
    username: str | None = None