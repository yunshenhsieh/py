import pymongo

def connect_mongo():

    client = pymongo.MongoClient("mongodb://root:example@yun_mongodb:27017")
    db = client.test
    collection_test = db.test
    # 插入資料
    simple_data={"123":"456"}
    post = {"author": "bruce",
	          "text": "My first blog post!",
              "tags": ["mongodb", "python", "pymongo"]}

    data_id = collection_test.insert_one(simple_data).inserted_id
    data_id = collection_test.insert_one(post).inserted_id
    # 查詢資料    
    print(collection_test.find())
    # 更新資料
    collection_test.update({"author":"bruce"},{'$set':{"text":'i love py'}})
    print('更新後：'collection_test.find())
    # 刪除資料
    collection_test.delete_one(simple_data)
    print('刪除後：'collection_test.find())

    return str(data_id)