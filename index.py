#this file is the main file of this fastApi project

from fastapi import FastAPI

from routes.product import router as productRouter
from routes.user import router as userRouter

app = FastAPI()

app.include_router(productRouter, prefix="/products", tags=["products"])

app.include_router(userRouter, prefix="/users", tags=["users"])