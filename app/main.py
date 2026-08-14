from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

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


app = FastAPI(title="Service API")


@app.get("/products", response_model=list[ProductRead])
def get_products(db: Session = Depends(get_db)):
	return get_all_products(db)


@app.get("/products/{product_id}", response_model=ProductRead)
def get_product_by_id(product_id: int ,db: Session = Depends(get_db)):
	product = get_product_by_id_repo(product_id, db)

	if product is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такого продукта нет",
		)

	return product


@app.post("/products", response_model=ProductRead)
def create_product(product_data: ProductCreate, db: Session = Depends(get_db)):
	return create_product_service(product_data, db)


@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):	
	product = delete_product_repo(product_id, db)

	if product is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такого продукта нет",
		)
	
	return {"message": "Successfully deleted"}


@app.patch("/products/{product_id}", response_model=ProductRead)
def update_product(data: ProductUpdate, product_id: int, db: Session = Depends(get_db)):
	product = update_product_service(product_id, data, db)

	if product is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такого продукта нет",
		)

	return product
