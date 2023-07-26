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
    print('in add')
    response = conn.ecom.products.insert_one(product.dict())
    print(response)
    return {"status":200, "message": "Student added successfully!"}

@router.get('/{id}')
async def getProduct(id: str):
    response = conn.ecom.products.find_one({"_id":ObjectId(id)})
    response['_id'] = str(response['_id'])
    return response    

@router.delete('/delete/{id}')
def deleteProduct(id:str):
    response = conn.ecom.products.delete_one({"_id": ObjectId(id)})
    print(response)
    return {"status":200, "message": "Product Successfully Deleted."}