def create_document(collection , document):
    document_dict = document.dict()
    collection.insert_one(document_dict)
    return document


def read_all_documents(collection):
    result = list(collection.find())
    print(result)
    return result
    

def read_document(collection , property: str , value: str):
    db_filter = {property : value}
    result = collection.find_one(db_filter)
    print(result)
    return result


def update_document(collection, id, new_document):
    filter = { "_id": id }
    newvalues = { "$set": new_document.dict() }
    if not collection.find_one(filter):
        return False
    collection.update_one(filter, newvalues)
    return new_document
    

def delete_document(collection, id):
    filter = { "_id": id }
    if not collection.find_one(filter):
        return False
    deleted_document = collection.delete_one(filter)
    return deleted_document

def search(collection, dict_of_filter: dict):
    result = collection.find({dict_of_filter})
    return result