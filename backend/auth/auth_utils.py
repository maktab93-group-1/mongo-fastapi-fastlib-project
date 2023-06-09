from passlib.context import CryptContext
from schemas.users import CreateUser

# pwd_context for password encryption
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db_collection, username: str):
    if username in db_collection:
        user_dict = db_collection.find({"username": username})
        return CreateUser(**user_dict)
    return None

def authenticate_user(collection, username: str, password: str):
    user = get_user(collection, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user