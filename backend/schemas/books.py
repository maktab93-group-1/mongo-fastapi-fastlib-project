from pydantic import BaseModel


class CreateBook(BaseModel):
    title: str | None = None
    author: str | None = None
    publication_year: int | None = None
    genre: str | None = None
    availability_status: bool | None = True
    
class ReturnBook(BaseModel):
    title: str | None = None
    availability_status: bool | None = True