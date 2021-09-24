from pymongo import MongoClient
import os
from datetime import *
import json
from tweet_collector import tweet_collector

with open("./auth_info.json", mode="r", encoding="utf-8") as f:
    auth_info = json.load(f)

collector = tweet_collector(auth_info["api_key"], auth_info["api_secret"],auth_info["access_token"], auth_info["access_secret"])

hashtags = ["#100日後に退職する47歳"]
tweets = collector.get_tweet(hashtags)

db_host = os.environ['MONGO_DB_HOST']
db_user = os.environ['MONGO_DB_USERNAME']
db_pass = os.environ['MONGO_DB_PASSWORD']
db_name = os.environ['MONGO_DB_DATABASE']
with MongoClient(db_host, 27017, username=db_user, password=db_pass) as client:
    tweet_db = client[db_name]
    tweet_collection = tweet_db.tweets

    for tweet in tweets:
        tweet_collection.insert_one(tweet)
