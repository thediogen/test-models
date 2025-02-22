from enum import Enum as stdEnum
import uuid

from sqlalchemy import String, Enum as saEnum, Integer, ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base


class CartItem(Base):
    __tablename__ = 'cart_items'
    
    product_title: Mapped[str] = mapped_column()
    product_description: Mapped[str] = mapped_column()
    product_price: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()

    product_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('productbases.id'))
    cart_id: Mapped[uuid.UUID] = mapped_column(ForeignKey('carts.id'))

    product = relationship('ProductBase')
    cart: Mapped['Cart'] = relationship('Cart', back_populates='cart_items', lazy='joined')
