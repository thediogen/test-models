from enum import Enum as stdEnum
import uuid

from sqlalchemy import String, Enum as saEnum, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.product_base import ProductBase


class Painting(ProductBase):
    id: Mapped[uuid.UUID] = mapped_column(ForeignKey('productbases.id'), primary_key=True)

    description: Mapped[str] = mapped_column()
    available: Mapped[int] = mapped_column()
    size: Mapped[dict] = mapped_column(JSON)

    __mapper_args__ = {
        'polymorphic_identity': 'painting',
    }
