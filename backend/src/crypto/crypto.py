import jwt
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from src import config

SECRET = config.SECRET
ALGORITHM = "HS256"

# for hashing
pwd_context = CryptContext(schemes=["scrypt"], deprecated="auto")

# token retrieval
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


# # Mock database of users (replace with your user database logic)
# fake_users_db = {
#     "admin": {
#         "username": "admin",
#         "password": "$scrypt$ln=16,r=8,p=1$ZUxJiZHyfu+9N6a0tjamFA$wDaTV+m273WsUPZGXtjoqOCZL4bgB5ITJgTYqIn8t3I",
#         "is_active": True,
#     }
# }

def verify(password, hashed_password) -> bool:
    return pwd_context.verify(secret=password, hash=hashed_password)


def get_password_hash(s: str) -> str:
    return pwd_context.hash(s)


def create_access_token(data: dict) -> str:
    return jwt.encode(data, SECRET, algorithm=ALGORITHM)


# Dependency for extracting and verifying JWT token
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        username: str = payload.get("username")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        token_data = {"username": username}
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return token_data
