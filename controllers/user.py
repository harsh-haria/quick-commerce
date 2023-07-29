from bson import ObjectId

from config import db,client

class User:
    def addNewUser(user):
        try:
            response = db.users.insert_one(user.dict())
            return {"status":200, "message": "Success"}
        except Exception as error:
            print(error)
            return {"status":500, "message":"An error occured while adding a new user"}
    
    async def getUserDetails(id):
        try:
            response = await client.ecom.users.find({"_id":ObjectId(id)})
            for item in response:
                item['_id'] = str(item['_id'])
            return response
        except Exception as error:
            print(error)
            return {"status":500, "message":"An error occured while fetching user data"}
        
    def addProductToUserCart(cart):
        response = db.users.update_one(
            {"_id": ObjectId(cart.userId)}, 
            { "$push": { "cart": ObjectId(cart.productId) } } 
        )
        print(response)
        return {"status":200, "message":"Success"}
    
    async def getUserCart(id):
        try:
            response = db.products.aggregate([
                { "$match": { "_id": ObjectId('64c2bd304e4dfc48baeba16c') } },
                { "$project": { "cart":1, "_id":0 } },
                {
                    "$lookup": {
                        "from": 'products',
                        "localField": 'cart',
                        "foreignField": '_id',
                        "as": 'cartDetails'
                    }
                },
                { "$project": {"cartDetails.title":1} }
            ])
            print(response)
            async for item in response:
                item['_id'] = str(item['_id'])
            return {"status":200, "message": "Success", "data": response}
        except Exception as error:
            print(error)
            return {"status":500, "message":"An error occured while getting cart details"}