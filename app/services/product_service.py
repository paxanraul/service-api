from sqlalchemy.orm import Session

from app.models import Product
from app.schemas import ProductCreate, ProductUpdate
from app.repositories.product_repo import create_product_repo, get_product_by_id_repo, save_product_repo


def create_product_service(product_data: ProductCreate, db: Session):
	product = Product(
		name=product_data.name,
		price=product_data.price,
		description=product_data.description,
	)

	return create_product_repo(product, db)


def update_product_service(product_id: int, product_data: ProductUpdate, db: Session):
	product = get_product_by_id_repo(product_id, db)

	if product is None:
		return None

	if product_data.name is not None:
		product.name = product_data.name

	if product_data.price is not None:
		product.price = product_data.price

	if product_data.description is not None:
		product.description = product_data.description

	return save_product_repo(product, db)
