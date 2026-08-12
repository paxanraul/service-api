from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ProductCreate(BaseModel):
	name: str
	price: Decimal
	description: str | None = None


class ProductRead(BaseModel):
	id: int
	name: str
	price: Decimal
	description: str | None = None

	model_config = ConfigDict(from_attributes=True)


class ProductUpdate(BaseModel):
	name: str | None = None
	price: Decimal | None = None
	description: str | None = None
