from datetime import date

from sqlalchemy import Enum , Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base


class Cart(Base):
    total_price: Mapped[int] = mapped_column()
    status: Mapped[str] = mapped_column(Enum('forming', 'waiting for accept', 'accepted', name='cart_status_enum'))
    created_at: Mapped[date] = mapped_column(Date, default=date.today)

    cart_items: Mapped[list["CartItem"]] = relationship(
        back_populates="cart", cascade="all, delete-orphan", lazy="joined"
    )
