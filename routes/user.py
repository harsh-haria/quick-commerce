from fastapi import APIRouter

from models.User import User
from models.AddToCard import AddToCard as AddToCartModel

from controllers.user import User as user_service

router = APIRouter()

@router.post('/addtocart/')
async def addProductToCart(cart:AddToCartModel):
    response = await user_service.addProductToUserCart(cart)
    if(response['status'] != 200):
        return response
    return {"status":200, "message": "Success"}

@router.post('/add')
async def addNewUser(user:User):
    response = await user_service.addNewUser(user)
    if(response['status'] != 200):
        return response
    return {"status":200, "message":"Success"}

@router.get('/{id}')
async def getUserDetails(id:str):
    response = await user_service.getUserDetails(id)
    if(response['status'] != 200):
        return response
    return {"status":200, "message":"Success", "data": response}

@router.get('/getUserCart/{id}')
async def getUserCart(id:str):
    print('in user cart')
    response = await user_service.getUserCart(id)
    if(response['status'] != 200):
        return response
    return {"status":200, "message":"Success", "data": response['data']}

@router.put('/removeProductFromCart')
async def removeProduct(id:str, product:str):
    response = await user_service.removeProductFromCart(id, product)
    if(response.status != 200):
        return response
    return {"status":200, "message":"Successfully removed the product from the cart."}

@router.post('/checkout')
async def checkoutCart(id:str):
    response = await user_service.checkout(id)
    if(response.status == 500):
        return response
    return {"status":200, "message":"Order created Successfully"}