from fastapi import APIRouter
from bson import ObjectId

from models.User import User
from models.AddToCard import AddToCard as AddToCartModel

from config import conn

from controllers.user import User as user_service

router = APIRouter()

@router.post('/addtocart/')
def addProductToCart(cart:AddToCartModel):
    response = user_service.addProductToUserCart(cart)
    if(response['status'] != 200):
        return response
    return {"status":200, "message": "Success"}

@router.post('/add')
def addNewUser(user:User):
    response = user_service.addNewUser(user)
    if(response['status'] != 200):
        return response
    return {"status":200, "message":"Success"}

@router.get('/{id}')
def getUserDetails(id:str):
    response = user_service.getUserDetails(id)
    if(response['status'] != 200):
        return response
    return {"status":200, "message":"Success", "data": response}