import pymongo
import json

db = pymongo.MongoClient().eb102

rows = db.lookup_product.aggregate([
    
    {'$unwind': "$sizes"}
     ,
    {
        '$lookup':
        {
          'from': "lookup_color",
          'localField': "sizes",
          'foreignField': "size",
          'as': "colors"
        }
    }
    ,
    {
      '$project':{
        "_id":0,
        "colors._id":0,
        "colors.size":0
      }
    }
])


for row in rows:
    print(json.dumps(row, indent=8))