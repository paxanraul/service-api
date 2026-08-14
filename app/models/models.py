from app.db import Base

from decimal import Decimal
from datetime import datetime
from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column

class Product(Base):
	__tablename__ = "products"

	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str] = mapped_column(String(20))
	price: Mapped[Decimal] = mapped_column(nullable=False)
	description: Mapped[str | None] = mapped_column(String(150))
	created_at: Mapped[datetime] = mapped_column(default=func.now())