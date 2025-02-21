from enum import Enum as stdEnum
import uuid

from sqlalchemy import String, Enum as saEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from fastapi import HTTPException, status

from backend.models.base import Base


class User(Base):
    username: Mapped[str] = mapped_column(String(64))
    email: Mapped[str] = mapped_column(String(128), unique=True)
    password: Mapped[str] = mapped_column()
    role: Mapped[str] = mapped_column(saEnum('admin', 'user', name='user_roles'), default='user')

    cart: Mapped[uuid.UUID] = mapped_column(ForeignKey('carts.id'))

