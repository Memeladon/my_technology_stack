from typing import Dict, Any, Optional, Type
from uuid import UUID
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, Query

from src.crypto.crypto import get_password_hash
from src.database.models import User

from base import BaseRepository


class UserRepositoryImpl(BaseRepository):
    def create_one(self, db: Session, data: Dict[str, Any]) -> User | None:
        try:
            new_one = User(**data, id=uuid.uuid4())
            new_one.password = get_password_hash(data['password'])
            db.add(new_one)
            db.commit()
            db.refresh(new_one)
            return new_one
        except SQLAlchemyError as e:
            db.rollback()
            raise f"Error CREATE user: {str(e)}"
        finally:
            db.close()

    def read_one(self, db: Session, user_id: UUID) -> User | None:
        try:
            user = db.query(User).filter(User.id == user_id).first()
            return user
        except SQLAlchemyError as e:
            raise f"Error READ user: {str(e)}"
        finally:
            db.close()

    def update_one(self, db: Session, user_id: UUID, user_data: Dict[str, Any]) -> Type[User]:
        try:
            user = db.query(User).filter(User.id == user_id).first()
            if not user:
                raise ValueError("User not found")

            for attr, value in user_data.items():
                setattr(user, attr, value)

            db.commit()
            return user
        except (SQLAlchemyError, ValueError) as e:
            db.rollback()
            raise f"Error UPDATE user: {str(e)}"
        finally:
            db.close()

    def delete_one(self, db: Session, user_id: UUID) -> bool:
        try:
            user = db.query(User).filter(User.id == user_id).first()
            if not user:
                raise ValueError("User not found")

            db.delete(user)
            db.commit()
            return True
        except (SQLAlchemyError, ValueError) as e:
            db.rollback()
            raise f"Error DELETE user: {str(e)}"
        finally:
            db.close()

    def delete_all(self, db: Session) -> bool:
        pass

    def list_all(self, db: Session):
        users = db.query(User).all()
        return users

    # TODO: Метод возвращает только одного юзера
    def search_by_something(self, db: Session, username: str, filter: Optional[str] = None) -> Type[User]:
        try:
            query = db.query(User)
            if username:
                query = query.filter(User.username == username)
            if filter:
                query = query.filter(User.username.contains(filter))
            return query.first()
        except SQLAlchemyError as e:
            raise f"Error READ LIST of users BY FILTER: {str(e)}"
        finally:
            db.close()

