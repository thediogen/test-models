from enum import Enum as stdEnum
import uuid

from sqlalchemy import String, Enum as saEnum
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base


class Painting(Base):
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
    available: Mapped[int] = mapped_column()
    