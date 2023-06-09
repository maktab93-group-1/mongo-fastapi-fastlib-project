from pydantic import BaseModel
# from bson import ObjectId

class CreateBook(BaseModel):
    title: str | None = None
    author: str | None = None
    publication_year: int | None = None
    genre: str | None = None
    availability_status: bool | None = True
    
class ReturnBook(BaseModel):
    id: str
    title: str | None = None
    availability_status: bool | None = True