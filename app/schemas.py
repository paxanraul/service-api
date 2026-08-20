from pydantic import BaseModel, ConfigDict, Field

from decimal import Decimal


class ProductCreate(BaseModel):
	name: str = Field(min_length=1, max_length=20)
	price: Decimal = Field(gt=0)
	description: str | None = Field(default=None, max_length=150)


class ProductRead(BaseModel):
	id: int
	name: str
	price: Decimal
	description: str | None = None

	model_config = ConfigDict(from_attributes=True)


class ProductUpdate(BaseModel):
	name: str | None = Field(default=None, min_length=1, max_length=20)
	price: Decimal | None = Field(default=None, gt=0)
	description: str | None = Field(default=None, max_length=150)
