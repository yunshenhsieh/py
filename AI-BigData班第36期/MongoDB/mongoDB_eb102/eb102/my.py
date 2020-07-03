import pprint
import pymongo
from pymongo import MongoClient
client = MongoClient()
db = client['eb102']
for i in db.coll3.find():
    pprint.pprint(i)