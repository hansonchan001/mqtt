import pymongo
from pymongo import MongoClient
cluster = MongoClient('mongodb+srv://root:root@cluster0.mlegxow.mongodb.net/?retryWrites=true&w=majority')
db = cluster["test"]
collection =db["student"]
post={"_id":0, "name":"hanson test"}
collection.insert_one(post)
