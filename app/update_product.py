from sqlalchemy import select

from app.db import SessionLocal
from app.models import Product


with SessionLocal() as session:
	statement = select(Product).where(Product.id == 1)
	product = session.scalar(statement)

	if product is not None:
		product.description = "Membrane keyboard"

		session.commit()
		session.refresh(product)
		print(product.description)
