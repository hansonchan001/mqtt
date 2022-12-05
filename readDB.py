import pymongo
from pymongo import MongoClient
import random

i = 0
mylist = []

cluster = MongoClient('mongodb+srv://root:root@cluster0.mlegxow.mongodb.net/?retryWrites=true&w=majority')
db = cluster["Exercise"]
collection =db["ex1"]

names = ['Peter', 'Ken', 'Paul', 'Alice', 'Eva', 'Martin', 'Scott', 'Walter']

for a in range(100):
    post = {
        'name': names[random.randint(0,7)],
        'age': random.randint(0,40),
    }
    mylist.append(post)


for i in range(len(mylist)):
    mylist[i]['_id'] = i
    print(mylist[i])

#x = collection.insert_many(mylist)



