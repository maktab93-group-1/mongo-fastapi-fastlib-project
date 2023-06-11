from crud.utils import create_document, read_document, search
from models.borrow import BorrowModel
from db import BOOKS
from schemas.books import CreateBook


def borrow(collection , user_id, book_id, start_date, end_date):
    new_borrow_obj = BorrowModel(book_id, user_id, start_date, end_date)
    requested_book: CreateBook = read_document(BOOKS, "id", book_id)
    if not requested_book.availability_status:
        return None
    requested_book.availability_status = False
    return create_document(collection , new_borrow_obj)

def return_book(collection, user_id, book_id, current_date):
    db_filter = { "book_id": book_id, "user_id": user_id}
    borrow_document = search(collection, db_filter)[0]
    
    if not borrow_document:
        return None
    if borrow_document.return_date < current_date:
        return "It is too late to return the book!"
    
    requested_book: CreateBook = read_document(BOOKS, "id", book_id)
    requested_book.availability_status = True
    
    return borrow_document    