from app.db import Base, engine
from app.models.product import Product

Base.metadata.create_all(engine)