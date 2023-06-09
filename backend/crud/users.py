from db import USERS
from crud.utils import create_document , read_all_documents , read_document

def create_user(collection,user):
    if user in list(collection.find()) :
        raise ValueError('username already exists')
    result = create_document(collection,user)
    return result


def read_user(collection , username , value):
    user = read_document(collection,username,value)
    return user
    


