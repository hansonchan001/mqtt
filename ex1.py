def get_database():
    from pymongo import MongoClient
    import pymongo
    import urllib

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    #CONNECTION_STRING = "mongodb+srv://hanson_OV:<XSW@3edc>@cluster0.mongodb.net/voltageSensor"
    mongo_url = 'mongodb+srv://root:root@cluster0.mlegxow.mongodb.net/?retryWrites=true&w=majority'

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(mongo_url)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['user_shopping_list']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()
    #print('hello')

    