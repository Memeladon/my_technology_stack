from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.crypto import crypto
from src.crypto.crypto import create_access_token, get_current_user
from src.database.models import get_db
from src.database.repositories.user import read_user_by_username

router = APIRouter(tags=['auth'], prefix='/auth')


@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    found_user = read_user_by_username(db, form_data.username)

    if not found_user:
        raise HTTPException(status_code=404, detail="No user with the username")

    if not crypto.verify(form_data.password, found_user.password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    access_token = create_access_token({"username": found_user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/protected/check")
def protected_route(current_user: dict = Depends(get_current_user)):
    return {"message": f"Beware, {current_user['username']}. This is a protected route."}
