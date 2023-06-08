from fastapi import APIRouter


book_router = APIRouter(prefix="/books")

@book_router.get("/")
def get_books():
    pass

@book_router.post("/")
def add_books():
    pass

@book_router.get("/{book_id}/")
def get_book():
    pass

@book_router.put("/{book_id}/")
def update_book():
    pass

@book_router.delete("/{book_id}/")
def delete_book():
    pass

@book_router.get("/search/")
def search_books(title:str = None, author: str = None, genre: str = None):
    pass

@book_router.put("/{book_id}/borrow/")
def borrow_book():
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

