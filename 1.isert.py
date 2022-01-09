import pymongo



if __name__ == "__main__":

        print("welcome to pymongo")
        client = pymongo.MongoClient("mongodb://localhost:27017")
        # print(client)

        db = client['pratik'] 
        # client
        collection = db['mySamplecode']
    

        # dictionary
        dictionary = [{'_id': 1,'name': 'ABC', 'marks': 50, 'adress': 'panvel1'},
                    {'_id': 2,'name': 'DEF', 'marks': 150, 'adress': 'panvel2'},
                    {'_id': 3,'name': 'GHIJ', 'marks': 250, 'adress': 'panvel3'},
                    {'_id': 4,'name': 'KLMN', 'marks': 350, 'adress': 'panvel4'}]
        # we can assign unique id by our selves

        # # inserting that data in dict
        # collection.insert_one(dictionary)

        collection.insert_many(dictionary)
