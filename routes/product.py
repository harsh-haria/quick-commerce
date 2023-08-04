from fastapi import APIRouter
from bson import ObjectId

from models.product import Product as productModel 
from models.product import UpdateProduct as updateModel

from controllers.product import Product

router = APIRouter()

product_service = Product()

@router.get("/getall")
async def get_all_products():
    return await product_service.getAllProducts()

@router.post('/add')
async def addNewProduct(product: productModel):
    response = await product_service.addNewProduct(product)
    if(response['status'] != 200):
        return response
    return {"status":200, "message":"Success"}

@router.get('/{id}')
async def getProduct(id: str):
    response = await product_service.getProduct(id)
    if(response['status'] != 200):
        return response
    return {"status":200, "message":"Success", "data":response['data']}

@router.delete('/delete/{id}')
def deleteProduct(id:str):
    response = product_service.deleteProduct(id)
    if(response != 200):
        return response
    return {"status":200, "message":"Success"}

@router.put('/updateProduct')
async def updateProduct(product:updateModel):
    productObject = dict(product)
    response = await product_service.updateProduct(productObject)
    if(response['status'] != 200):
        return response
    return {"status":200, "message":"Success"}