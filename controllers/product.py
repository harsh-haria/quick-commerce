from bson import ObjectId
from fastapi.encoders import jsonable_encoder
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

    async def getProduct(self, id):
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
        
    async def updateProduct(self, product):
        try:
            productId = product['id']
            updatedProduct = jsonable_encoder(product)
            # updatedProduct = {
            #     "title": product['title'],
            #     "productDescription": product['productDescription'],
            #     "brand": product['brand'],
            #     "modelNo": product['modelNo'],
            #     "mrp": product['mrp'],
            #     "costPrice": product['costPrice'],
            #     "sellingPrice": product['sellingPrice'],
            #     "seller": product['seller'],
            #     "countryOfOrigin": product['countryOfOrigin'],
            #     "genericName": product['genericName'],
            #     "manufacturer": product['manufacturer'],
            #     "sizeLength": product['sizeLength'],
            #     "weight": product['weight'],
            #     "category": product['category'],
            #     "dateFirstAvailable": product['dateFirstAvailable'],
            #     "reviews": product['reviews'],
            #     "netQuantityAvailable": product['netQuantityAvailable'],
            #     "netQuantityUnit": product['netQuantityUnit'],
            #     "categoryRank": product['categoryRank'],
            #     "manufacturingDate": product['manufacturingDate'],
            #     "expirationDate": product['expirationDate'],
            #     "isReturnable": product['isReturnable'],
            #     "vegNonveg": product['vegNonveg'],
            #     "isCertified": product['isCertified'],
            #     "extraDetailsBrand": product['extraDetailsBrand'],
            #     "warehouse": product['warehouse'],
            #     "productImages": product['productImages'],
            # }
            response = await db.products.update_one(
                {"_id":ObjectId(productId)},
                {"$set": updatedProduct }
            )
            return {"status":200, "message": "Product Successfully Updated.", "data":response}
        except Exception as error:
            print(error)
            return {"status":500, "message":"Some error occured while updating the product"}