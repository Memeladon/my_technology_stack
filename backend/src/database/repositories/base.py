from uuid import UUID
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session


class BaseRepository(ABC):
    @abstractmethod
    def create_one(self, db: Session, data: dict):
        pass

    @abstractmethod
    def read_one(self, db: Session, id: UUID | int):
        pass

    @abstractmethod
    def update_one(self, db: Session, id: UUID | int, new_data: dict):
        pass

    @abstractmethod
    def delete_one(self, db: Session, id: UUID | int) -> None:
        pass

    @abstractmethod
    def delete_all(self, db: Session) -> None:
        pass

    @abstractmethod
    def list_all(self, db: Session):
        pass

    @abstractmethod
    def search_by_something(self, db: Session, something: str | int):
        pass

