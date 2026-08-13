from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Product
from app.schemas import ProductCreate, ProductUpdate


def get_all_products(db: Session):
	statement = select(Product)
	products = db.scalars(statement).all()

	return products


def get_product_by_id_repo(product_id: int, db: Session):
	statement = select(Product).where(Product.id == product_id)
	product = db.scalar(statement)

	return product


def create_product_repo(product_data: ProductCreate, db: Session):
	product = Product(
		name=product_data.name,
		price=product_data.price,
		description=product_data.description,
	)
	db.add(product)
	db.commit()
	db.refresh(product)

	return product


def delete_product_repo(product_id: int, db: Session):
	statement = select(Product).where(Product.id == product_id)
	product = db.scalar(statement)

	if product is None:
		return None

	db.delete(product)
	db.commit()

	return product

def update_product_repo(data: ProductUpdate, product_id: int, db: Session):
	statement = select(Product).where(Product.id == product_id)
	product = db.scalar(statement)

	if product is None:
		return None

	if data.name is not None:
		product.name = data.name

	if data.price is not None:
		product.price = data.price

	if data.description is not None:
		product.description = data.description

	db.commit()
	db.refresh(product)

	return product
	