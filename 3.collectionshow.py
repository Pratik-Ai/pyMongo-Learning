import pymongo
from pymongo import collection



if __name__ == "__main__":

    print("welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    # print(client)

    db = client['pratik'] 
    # client
    collection = db['mySamplecode']
    s = collection.find_one()
    print(s)

    allData = client.list_database_names()
    print(allData)

    coll = client['pratik']
    print(coll.list_collection_names())