from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models import Product
from app.schemas import ProductRead


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
