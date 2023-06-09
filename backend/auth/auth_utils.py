from passlib.context import CryptContext
from schemas.users import CreateUser
from crud.users import read_user

# pwd_context for password encryption
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(collection, username: str, password: str):
    user = CreateUser(**read_user(collection, username))
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user