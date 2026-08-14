from app.db import Base, engine
from app.models.models import Product

Base.metadata.create_all(engine)