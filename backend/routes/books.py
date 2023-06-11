from fastapi import APIRouter, HTTPException , Depends
from schemas.books import CreateBook, ReturnBook , SerachSchema
from typing import List , Annotated
from crud.books import read_all_books, create_book, read_book, update_book, delete_book, search_book
from db import BOOKS
from bson import ObjectId
from auth.jwt_utils import get_current_user
from schemas.users import CreateUser

book_router = APIRouter(prefix="/books", tags=["books"])

@book_router.get("/", response_model=List[ReturnBook])
def get_books():
    var = read_all_books(BOOKS)
    lst = []
    for v in var:
        v['id'] = str(v.pop('_id'))
        lst.append(ReturnBook(**v))
    return lst

@book_router.post("/")
def add_books(book: CreateBook):
    return create_book(BOOKS, book)

@book_router.get("/{book_id}/")
def get_book(book_id: str):
    var = read_book(BOOKS, "_id", book_id)
    var['id'] = var.pop('_id')
    return ReturnBook(**var)

@book_router.put("/{book_id}/")
def update_book_in_db(book_id, updated_book: CreateBook):
    var = update_book(BOOKS, book_id, updated_book)
    if var:
        return {"message": "Book successfully updated!"}
    raise HTTPException(status_code=404, detail="bookID not found")

@book_router.delete("/{book_id}/")
def delete_book_in_db(book_id):
    var = delete_book(BOOKS, book_id)
    if var:
        return {"message": "Book successfully deleted!"}
    raise HTTPException(status_code=404, detail="bookID not found")

@book_router.get("/search/")
def search_books(model : SerachSchema):
    db_filter = {}
    if model.title:
        db_filter["title"] = model.title
    if model.author:
        db_filter["author"] = model.author
    if model.genre:
        db_filter["genre"] = model.genre
    result = search_book(BOOKS, db_filter)
    if not result:
        return {"message": "No books found!"}
    return result

@book_router.put("/{book_id}/borrow/")
def borrow_book(book_id:str , current_user: Annotated[CreateUser, Depends(get_current_user)]):
    pass

@book_router.put("/{book_id}/return/")
def return_book():
    pass

@book_router.get("/genres/")
def get_book_genres():
    pass

@book_router.get("/authors/")
def get_book_authors():
    pass

