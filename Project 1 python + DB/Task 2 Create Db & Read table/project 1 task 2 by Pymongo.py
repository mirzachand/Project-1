from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/', 27017)
print(client.list_database_names())

db = client['mobile']

collection = db['Brands']

list1 =[{"name":"Apple","position":1},{"name":"Samsung","position":2},{"name":"OnePlus","position":3},{"name":"Xiomi","position":4}]
res = collection.insert_many(list1)
print("modeile brands are added")
print(res.inserted_ids)

