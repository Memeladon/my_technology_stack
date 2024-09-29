import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase

DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not defined!")

engine = create_engine(
    url=DATABASE_URL
)


session = sessionmaker(engine, expire_on_commit=False)


def get_db() -> Session:
    db = session()
    try:
        yield db
    finally:
        db.close()


class Base(DeclarativeBase):
    pass
