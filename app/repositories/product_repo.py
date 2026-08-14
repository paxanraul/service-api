from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Product


def get_all_products(db: Session):
	statement = select(Product)
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
	