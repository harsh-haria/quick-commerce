from bson import ObjectId

from config import conn

class User:
    def addNewUser(user):
        try:
            response = conn.ecom.users.insert_one(user.dict())
            return {"status":200, "message": "Success"}
        except Exception as error:
            print(error)
            return {"status":500, "message":"An error occured while adding a new user"}
    
    def getUserDetails(id):
        try:
            response = conn.ecom.users.find({"_id":ObjectId(id)})
            for item in response:
                item['_id'] = str(item['_id'])
            return response
        except Exception as error:
            print(error)
            return {"status":500, "message":"An error occured while fetching user data"}
        
    def addProductToUserCart(cart):
        response = conn.ecom.users.update_one(
            {"_id": ObjectId(cart.userId)}, 
            { "$push": { "cart": ObjectId(cart.productId) } } 
        )
        print(response)
        return {"status":200, "message":"Success"}