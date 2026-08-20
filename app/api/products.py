from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from decimal import Decimal

from app.dependencies import get_db
from app.schemas import ProductRead, ProductCreate, ProductUpdate
from app.repositories.product_repo import (
	get_all_products, 
	get_product_by_id_repo, 
	delete_product_repo,
)
from app.services.product_service import (
	create_product_service, 
	update_product_service,
)

router = APIRouter(prefix="/products", tags=["products"])


@router.get("", response_model=list[ProductRead])
def get_products(
	db: Session = Depends(get_db), 
	limit: int = Query(default=5, ge=1, le=100),
	offset: int = Query(default=0, ge=0),
	min_price: Decimal | None = None,
	max_price: Decimal | None = None,
	name: str | None = Query(default=None, min_length=1, max_length=20),
):
	if min_price is not None and max_price is not None:
		if min_price > max_price:
			raise HTTPException(
				status_code=status.HTTP_400_BAD_REQUEST,
				detail="Минимальная цена не может быть больше максимальной!"
			)
	
	return get_all_products(db, limit, offset, min_price, max_price, name)


@router.get("/{product_id}", response_model=ProductRead)
def get_product_by_id(product_id: int ,db: Session = Depends(get_db)):
	product = get_product_by_id_repo(product_id, db)

	if product is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такого продукта нет",
		)

	return product


@router.post("", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
def create_product(product_data: ProductCreate, db: Session = Depends(get_db)):
	return create_product_service(product_data, db)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):	
	product = delete_product_repo(product_id, db)

	if product is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такого продукта нет",
		)
	

@router.patch("/{product_id}", response_model=ProductRead)
def update_product(data: ProductUpdate, product_id: int, db: Session = Depends(get_db)):
	product = update_product_service(product_id, data, db)

	if product is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такого продукта нет",
		)

	return product
