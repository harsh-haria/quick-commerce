from bson import ObjectId

from config import db


class Product:
    async def addNewProduct(self, product):
        try:
            response = await db.products.insert_one(product.dict())
            print(response)
            return {"status":200, "message": "Student added successfully!"}
        except Exception as error:
            print(error)
            return {"status":500, "message":"An Error occured while adding a new product"}

    async def getAllProducts(self):
        try:
            print('in get products')
            response = db.products.find({})
            productList = []
            async for document in response:
                document['_id'] = str(document['_id'])
                productList.append(document)
            return productList
        except Exception as error:
            print(error)
            return {"status":500, "message":"Some Error occoured while getting product details"}

    async def getProduct(self,id):
        try:
            response = await db.products.find_one({"_id":ObjectId(id)})
            if(response):
                response['_id'] = str(response['_id'])
                return {"status":200, "data":response}
            else:
                return {"status":200, "data":[]}
        except Exception as error:
            print(error)
            return {"status":500, "message":"Some Error occoured while getting product details"}
    
    async def deleteProduct(self, id):
        try:
            response = await db.products.delete_one({"_id": ObjectId(id)})
            return {"status":200, "message": "Product Successfully Deleted."}
        except Exception as error:
            print(error)
            return {"status":500, "message":"Some error occured while deleting product"}
        
    def updateProduct():
        return ''