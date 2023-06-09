def create_document(collection , document):
    try :
        document_dict = document.dict()
        collection.insert_one(document_dict)
        return True
    except:
        return False
    
def read_all_documents(collection):
    try :
        result = list(collection.find())
        return result
    except:
        return None
    

def read_document(collection , property , value):

    result = list(collection.find({property : value}))
    return result


