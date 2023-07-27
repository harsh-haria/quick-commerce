from fastapi import APIRouter

from models.User import User

from config import conn

router = APIRouter()

@router.post('/add')
def addNewUser(user:User):
    return user

@router.get('/{id}')
def getUserDetails(id:str):
    response = conn.ecom.users.find({})
    for item in response:
        item['_id'] = str(item['_id'])
    return response