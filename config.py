from pymongo import MongoClient
from util.secrets import mongodb

conn = MongoClient(mongodb)
try:
    # Send a ping to confirm a successful connection
    conn.admin.command('ping')
    print("Connected!")
except Exception as e:
    print(e)
