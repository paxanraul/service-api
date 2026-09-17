from fastapi import FastAPI

from app.api.products import router as products_router
from app.api.health import router as health_router
from app.api.users import router as users_router


app = FastAPI(title="Service API")

app.include_router(users_router)
app.include_router(products_router)
app.include_router(health_router)
