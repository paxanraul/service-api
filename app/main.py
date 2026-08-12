from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models import Product
from app.schemas import ProductRead, ProductCreate, ProductUpdate


app = FastAPI(title="Service API")


@app.get("/products", response_model=list[ProductRead])
def get_products(db: Session = Depends(get_db)):
	statement = select(Product)
	products = db.scalars(statement).all()

	products_list = []

	for product in products:
		product_data = {
			"id": product.id,
			"name": product.name,
			"price": product.price,
			"description": product.description,
		}
		products_list.append(product_data)

	return products_list


@app.get("/products/{product_id}", response_model=ProductRead)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
	statement = select(Product).where(Product.id == product_id)
	product = db.scalar(statement)

	if product is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такого продукта нет",
		)

	return product


@app.post("/products", response_model=ProductRead)
def create_product(product_data: ProductCreate, db: Session = Depends(get_db)):
	product = Product(
		name=product_data.name,
		price=product_data.price,
		description=product_data.description,
	)
	db.add(product)
	db.commit()
	db.refresh(product)

	return product


@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
	statement = select(Product).where(Product.id == product_id)
	product = db.scalar(statement)

	if product is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такого продукта нет",
		)
	
	db.delete(product)
	db.commit()

	return {"message": "Successfully deleted"}


@app.patch("/products/{product_id}", response_model=ProductRead)
def update_product(data: ProductUpdate, product_id: int, db: Session = Depends(get_db)):
	statement = select(Product).where(Product.id == product_id)
	product = db.scalar(statement)

	if product is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Такого продукта нет",
		)

	if data.name is not None:
		product.name = data.name
	if data.price is not None:
		product.price = data.price
	if data.description is not None:
		product.description = data.description

	db.commit()
	db.refresh(product)

	return product
