from bson import ObjectId

from config import conn


class Product:
    def addNewProduct(self, product):
        try:
            response = conn.ecom.products.insert_one(product.dict())
            print(response)
            return {"status":200, "message": "Student added successfully!"}
        except Exception as error:
            print(error)
            return {"status":500, "message":"An Error occured while adding a new product"}

    def getProduct(self,id):
        try:
            response = conn.ecom.products.find_one({"_id":ObjectId(id)})
            if(response):
                response['_id'] = str(response['_id'])
                return {"status":200, "data":response}
            else:
                return {"status":200, "data":[]}
        except Exception as error:
            print(error)
            return {"status":500, "message":"Some Error occoured while getting product details"}
    
    def deleteProduct(self, id):
        try:
            response = conn.ecom.products.delete_one({"_id": ObjectId(id)})
            return {"status":200, "message": "Product Successfully Deleted."}
        except Exception as error:
            print(error)
            return {"status":500, "message":"Some error occured while deleting product"}