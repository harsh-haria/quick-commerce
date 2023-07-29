import motor.motor_asyncio

from util.secrets import mongodb as MONGODB_URI

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)

if client:
    print('client', client)
    print("MongoDB connection successful.")
else:
    print("connection failed!")

db = client["ecom"]