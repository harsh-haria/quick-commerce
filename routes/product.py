from fastapi import APIRouter
from controllers.product import Product
from bson import ObjectId

from models.product import Product as productModel 

from config import conn

router = APIRouter()

product_service = Product()

@router.get("/getall")
def get_all_products():
    return product_service.getProduct()

@router.post('/add')
def addNewProduct(product: productModel):
    response = product_service.addNewProduct(product)
    if(response['status'] != 200):
        return response
    return {"status":200, "message":"Success"}
    

@router.get('/{id}')
async def getProduct(id: str):
    response = product_service.getProduct(id)
    if(response['status'] != 200):
        return response
    return {"status":200, "message":"Success", "data":response['data']}

@router.delete('/delete/{id}')
def deleteProduct(id:str):
    response = product_service.deleteProduct(id)
    if(response != 200):
        return response
    return {"status":200, "message":"Success"}