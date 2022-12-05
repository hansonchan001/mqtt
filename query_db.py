import sys
from pymongo import MongoClient
import matplotlib.pyplot as plt
import numpy as np

cluster = MongoClient('mongodb+srv://root:root@cluster0.mlegxow.mongodb.net/?retryWrites=true&w=majority')
db = cluster["battery"]
collection =db["voltage"]

month = int(sys.argv[1])
day = int(sys.argv[2])
time = sys.argv[3]
#minute_lt = int(sys.argv[4])

n = []
v = []
t = []

myquery = {"month": month,
          "day": day,
          "time":{"$lt":time}}

for x in collection.find(myquery, {"_id": 0}):
  if (x not in n):
    n.append(x)
    try:
      v.append(float(x["volt"]))
      t.append(int(x["time"]))
    except:
      continue


 
for a in n:
  print(a)

print(len(n))


x=np.array(t)
y=np.array(v)

fig, ax = plt.subplots()
ax.scatter(x, y, c="blue", alpha=0.5)
ax.set_xlabel("Time")
ax.set_ylabel("Volt")
ax.legend()
plt.show()







