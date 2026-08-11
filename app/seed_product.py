from decimal import Decimal

from app.db import SessionLocal
from app.models import Product


with SessionLocal() as session:
	product = Product(
		name="Keyboard",
		price=Decimal("99.99"),
		description="Mechanical keyboard",
	)

	session.add(product)
	session.commit()
	session.refresh(product)

	print(product.id)