from crud.utils import create_document, read_document, \
    read_all_documents, update_document, delete_document, search_by_property
from schemas.books import ReturnBook

def create_book(collection, new_book):
    return create_document(collection, new_book)


def read_book(collection, id, value):
    return read_document(collection, id, value)


def read_all_books(collection):
    return read_all_documents(collection)


def update_book(collection, book_id, new_book):
    return update_document(collection, book_id, new_book)


def delete_book(collection, book_id):
    return delete_document(collection, book_id)


# def search_book_by_property(collection, dct):
#     return search_by_property({'genre': genre})