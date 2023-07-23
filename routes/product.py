from fastapi import APIRouter, Depends
from controllers.product import Product

router = APIRouter()

product_service = Product()

@router.get("/getall")
def get_all_products():
    return product_service.getProduct()