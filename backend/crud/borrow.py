from crud.utils import create_document
from db import BORROW

def borrow(collection , document):
    create_document(collection , document)