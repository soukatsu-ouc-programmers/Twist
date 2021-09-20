from pymongo import MongoClient
import os
from datetime import *

# client = MongoClient('mongodb://db:27017/')
db_host = os.environ['MONGO_DB_HOST']
db_user = os.environ['MONGO_DB_USERNAME']
db_pass = os.environ['MONGO_DB_PASSWORD']
db_name = os.environ['MONGO_DB_DATABASE']
with MongoClient(db_host, 27017, username=db_user, password=db_pass) as client:
    tweet_db = client[db_name]
    tweet_collection = tweet_db.tweets

    tweet_collection.insert_one({
        "id": "1438301756174356483",
        "date": datetime.strptime('Thu Sep 16 00:40:00 +0000 2021', '%a %b %d %H:%M:%S %z %Y').astimezone(
            timezone(timedelta(hours=+9))),
        "hashtag": ["test1", "test2"]})
