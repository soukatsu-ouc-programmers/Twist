from pymongo import MongoClient
import os

# client = MongoClient('mongodb://db:27017/')
db_host = os.environ['MONGO_DB_HOST']
db_user = os.environ['MONGO_DB_USERNAME']
db_pass = os.environ['MONGO_DB_PASSWORD']
with MongoClient(db_host, 27017, username=db_user, password=db_pass) as client:
    test_db = client.tweet_db
    test_collection = test_db.test_collection

    test_collection.insert_one({"name": "test", "age": 24, "tag": ["test1", "test2"]})
