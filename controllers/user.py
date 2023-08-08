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
            response = db.users.aggregate([
                { "$match": { "_id": ObjectId(id) } },
                {
                    "$lookup": {
                        "from": 'products',
                        "localField": 'cart',
                        "foreignField": '_id',
                        "as": 'cartDetails'
                    }
                },
                { "$project": {"cartDetails":1, "_id":0} }
            ])
            itemList = []
            async for item in response:
                for document in item['cartDetails']:
                    document['_id'] = str(document['_id'])
                    itemList.append(document)
            return {"status":200, "message": "Success", "data": itemList}
        except Exception as error:
            print(error)
            return {"status":500, "message":"An error occured while getting cart details"}
        
    async def removeProductFromCart(id, product):
        try:
            response = await db.users.updateOne(
                { "_id" : ObjectId(id) },
                { "$pull": { "cart": ObjectId(product) } }
            )
            print(response)
            return {"status":200, "message":"Success"}
        except Exception as error:
            print(error)
            return {"status":500, "message":"An error occured while removing the product"}
    
    async def checkout(userId):
        """
            {
                "user":ObjectId('123abcd'),
                "deliveryAddress":{
                    "room":105,
                    "floor":10,
                    "building":"Hirani Towers",
                    "road" : "LBS Road",
                    "landmark": "Opposite SDK Hospital"
                },
                "orderDate":"1970-01-01T00:00:00.000Z",
                "orderValue": 1233.55,
                "paymentMethod": "Card",
                "orderStatus": "Complete",
                "invoice": "www.xyz.com/prod/images/uuid.pdf",
                "items": [ ObjectId('123123123'), ObjectId('456745674') ]
            }
        """
        try:
            orderIds = db.users.aggregate([
                {"$match":{"_id": ObjectId(userId) }},
                {"$project": {"cart":1,"_id":0}}
            ])
            itemList = []
            async for item in orderIds:
                print(item)
                for document in item['cart']:
                    document = str(document)
                    itemList.append(document)
            #get products to calculate final order value

            #caluculate stuff required

            #create the final object

            #insert the object
            createOrder = db.orders.insert_one()
            return {"status":200, "message":"Success"}
        except Exception as error:
            print(error)
            return {"status":500, "message":"An error occured while checking the order out"}

    def getPrevOrders():
        return ''