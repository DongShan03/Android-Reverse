from pymongo import MongoClient


def get_db():
    client = MongoClient(host="localhost", port=27017) #默认端口为27017
    # admin = client['admin']
    # admin.authenticate("username", "password")
    db = client["test"]
    return db


def add_one(data):
    db = get_db()
    result = db["teacher"].insert_one({"name": "alex", "age": 18})
    # result = db["teacher"].insert_many({"name": "alex", "age": 18})
    print(result)
    return result

def update(collection_name, condition, prepare):
    db = get_db()
    result = db[collection_name].update_one(condition, prepare)
    # result = db[collection_name].update_many(condition, prepare)
    return result

def delete(collection_name, condition):
    db = get_db()
    result = db[collection_name].delete_many(condition)
    return result

def query(collection_name, condition):
    db = get_db()
    result = db[collection_name].find(condition)
    # for item in result:
    #     print(item)
    return list(result)

if __name__ == "__main__":
    get_db()
    add_one(1)
    update("teacher", {"name": "alex"}, {"$set": {"age":777}})
    delete("teacher", {"age": 777})