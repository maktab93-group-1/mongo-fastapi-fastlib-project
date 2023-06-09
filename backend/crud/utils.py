def create_document(collection , document):
    document_dict = document.dict()
    collection.insert_one(document_dict)
    return document


def read_all_documents(collection):
    result = list(collection.find())
    return result
    

def read_document(collection , property , value):

    result = list(collection.find({property : value}))
    return result


def update_document(collection, id, new_document):
    filter = { "_id": id }
    newvalues = { "$set": new_document.dict() }
    collection.update_one(filter, newvalues)
    return new_document
    

def delete_document(collection, id):
    filter = { "_id": id }
    deleted_document = collection.delete_one(filter)
    return deleted_document
