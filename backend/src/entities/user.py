from enum import StrEnum
from uuid import UUID

from pydantic import BaseModel


class UserRole(StrEnum):
    ADMIN = 'ADMIN'
    USER = 'USER'


class User(BaseModel):
    id: UUID
    username: str
    password: str
    role: str
    is_active: bool


class UserCreate(BaseModel):
    username: str
    password: str
    role: str
    is_active: bool


class UserUpdate(BaseModel):
    username: str
    role: str
    is_active: bool


class UserResponse(BaseModel):
    id: UUID
    username: str
    role: str
    is_active: bool


class UserAuth(BaseModel):
    username: str
    password: str
