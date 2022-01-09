import pymongo
from pymongo import collection



if __name__ == "__main__":

    print("welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    # print(client)

    db = client['pratik'] 
    # client
    collection = db['mySamplecode']
    # dictionary
    dictionary = [{'name': 'ABC', 'marks': 50, 'adress': 'panvel1'},
                   {'name': 'DEF', 'marks': 150, 'adress': 'panvel2'},
                   {'name': 'GHIJ', 'marks': 250, 'adress': 'panvel3'},
                   {'name': 'KLMN', 'marks': 350, 'adress': 'panvel4'}]

    # # inserting that data in dict
    # collection.insert_one(dictionary)
    
    collection.insert_many(dictionary)

