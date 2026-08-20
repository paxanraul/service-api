from sqlalchemy import select
from sqlalchemy.orm import Session
from decimal import Decimal

from app.models.models import Product


def get_all_products(
		db: Session, 
		limit: int = 5, 
		offset: int = 0, 
		min_price: Decimal | None = None, 
		max_price: Decimal | None = None,
		name: str | None = None
):
	statement = select(Product)

	if min_price is not None:
		statement = statement.where(Product.price >= min_price)

	if max_price is not None:
		statement = statement.where(Product.price <= max_price)

	if name is not None:
		statement = statement.where(Product.name.ilike(f"%{name}%"))

	statement = statement.order_by(Product.price.desc()).limit(limit).offset(offset)
	products = db.scalars(statement).all()

	return products


def get_product_by_id_repo(product_id: int, db: Session):
	statement = select(Product).where(Product.id == product_id)
	product = db.scalar(statement)

	return product


def create_product_repo(product: Product, db: Session):
	try:
		db.add(product)
		db.commit()
		db.refresh(product)	
	except Exception:
		db.rollback()
		raise

	return product


def delete_product_repo(product_id: int, db: Session):
	statement = select(Product).where(Product.id == product_id)
	product = db.scalar(statement)

	if product is None:
		return None

	try:
		db.delete(product)
		db.commit()
	except Exception:
		db.rollback()
		raise

	return product

def update_product_repo(product_id: int, db: Session):
	statement = select(Product).where(Product.id == product_id)
	product = db.scalar(statement)

	try:
		db.commit()
		db.refresh(product)
	except Exception:
		db.rollback()
		raise

	return product


def save_product_repo(product: Product, db: Session):
	try:
		db.commit()
		db.refresh(product)
	except Exception:
		db.rollback()
		raise

	return product
	