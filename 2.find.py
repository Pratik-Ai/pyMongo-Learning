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
    t = collection.find_one({'name':'ABC'})
    print(t)

    allDocs = collection.find({'name':'ABC'})
    for i in allDocs:
        print(i)
    
    print("\n\n\n\n\n")
    # # here we are givin filter about what to show and what to not 1 - show and 0 - hide
    
    adoc = collection.find({'name':'ABC'} , {'name': 1,'_id' : 0})
    for i in adoc:
        print(i)

    allData = client.list_database_names()
    print(allData)