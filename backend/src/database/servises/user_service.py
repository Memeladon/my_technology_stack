from typing import Optional, Type
from sqlalchemy.orm import Session, Query
from uuid import UUID

from src.database.repositories import UserRepositoryImpl
from src.database.models import User


class UserServ:
    @staticmethod
    def create_user(db: Session, data: dict) -> User:
        user_repo = UserRepositoryImpl()
        return user_repo.create_one(db, data)

    @staticmethod
    def read_user_by_id(db: Session, id: UUID) -> Optional[User]:
        user_repo = UserRepositoryImpl()
        return user_repo.read_one(db, id)

    @staticmethod
    def read_user_by_username(db: Session, username: str, filter: Optional[str] = None) -> Type[User]:
        user_repo = UserRepositoryImpl()
        return user_repo.search_by_something(db, username, filter)

    @staticmethod
    def read_all_users(db: Session) -> list[Type[User]]:
        user_repo = UserRepositoryImpl()
        return user_repo.list_all(db)

    @staticmethod
    def update_user(db: Session, id: UUID, new_data: dict) -> Type[User]:
        user_repo = UserRepositoryImpl()
        return user_repo.update_one(db, id, new_data)

    @staticmethod
    def delete_user(db: Session, id: UUID) -> bool:
        user_repo = UserRepositoryImpl()
        return user_repo.delete_one(db, id)

    @staticmethod
    def delete_all_users(db: Session) -> bool:
        user_repo = UserRepositoryImpl()
        return user_repo.delete_all(db)
