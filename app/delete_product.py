from sqlalchemy import select, delete

from app.db import SessionLocal
from app.models.models import Product


with SessionLocal() as session:
	statement = select(Product).where(Product.id == 1)
	product = session.scalar(statement)

	if product is not None:
		session.delete(product)
		session.commit()
		print("Successfully deleted!")
