#this file is the main file of this fastApi project

from fastapi import FastAPI

from routes.product import router as productRouter

app = FastAPI()

app.include_router(productRouter, prefix="/products", tags=["products"])