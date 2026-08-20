from fastapi import FastAPI

from app.api.products import router as products_router


app = FastAPI(title="Service API")

app.include_router(products_router)
