from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel

class ProductCreate(BaseModel):
	name: str
	price: float
	description: str | None = None


products = [
	{"name": "MacBook pro", "price": 120000}
]


app = FastAPI()


def get_current_user():
	return {"name": "Raul", "role": "admin"}


def require_admin(admin = Depends(get_current_user)):
	if admin["role"] != "admin":
		raise HTTPException(
			status_code=status.HTTP_403_FORBIDDEN,
			detail="User is not admin"
		)
	return admin


@app.post("/products")
def create_product(product: ProductCreate):
	products.append(product.model_dump())
	return product


@app.get("/products")
def get_products(min_price: float | None = None):
	filtered_products = []

	for product in products:
		if min_price is not None and product["price"] < min_price:
			continue

		filtered_products.append(product)

	return filtered_products
	


@app.get("/admin")
def get_admin(current_user = Depends(require_admin)):
	return current_user
