from sqlalchemy import select

from app.db import SessionLocal
from app.models import Product


with SessionLocal() as session:
	statement = select(Product)
	products = session.scalars(statement).all()

	for product in products:
		print(product.id, product.name, product.price, product.description)
