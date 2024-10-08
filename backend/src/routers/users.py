from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.models import get_db
from src.database.servises import UserServ
from src.entities.user import UserCreate, UserUpdate

router = APIRouter(tags=['users'], prefix='/users')


@router.get('/')
def get_all_users(db: Session = Depends(get_db)):
    return UserServ.read_all_users(db)


@router.get('/{id}')
def get_one_user_by_id(id, db: Session = Depends(get_db)):
    return UserServ.read_user_by_id(db, id)


@router.post('/')
def create_one_user(data: UserCreate, db: Session = Depends(get_db)):
    return UserServ.create_user(db, data.dict())


@router.put('/{id}')
def update_one_user(id, data: UserUpdate, db: Session = Depends(get_db)):
    return UserServ.update_user(db, id, data.dict())


@router.delete('/{id}')
def delete_one_user(id, db: Session = Depends(get_db)):
    return delete_one_user(db, id)
