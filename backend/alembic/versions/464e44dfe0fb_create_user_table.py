"""create user table

Revision ID: 464e44dfe0fb
Revises: 6e1c8aa9edde
Create Date: 2024-09-29 04:50:42.054483

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import table


# revision identifiers, used by Alembic.
revision: str = '464e44dfe0fb'
down_revision: Union[str, None] = '6e1c8aa9edde'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


USERS = table("users", sa.Column('id', sa.Uuid(), nullable=False),
              sa.Column('username', sa.String(), nullable=False),
              sa.Column('password', sa.String(), nullable=False),
              sa.Column('role', sa.String(), nullable=False),
              sa.Column('is_active'))

USER_ID = "ae7ee1ee-fade-4c11-afc0-53a702780211"


def upgrade() -> None:
    op.bulk_insert(USERS, [
        {
            "id": USER_ID,
            "username": "admin",
            "password": "$scrypt$ln=16,r=8,p=1$wXjP+X8v5Tzn3BsjRGhNiQ$OMVKqmnCnrR324quXK8U4L0FIUQBjhT5pv+6Ox9Jl1M",
            "role": "ADMIN",
            "is_active": "true"
        }
    ])
    pass


def downgrade() -> None:
    op.execute(USERS.delete().where(USERS.c.id == USER_ID))
