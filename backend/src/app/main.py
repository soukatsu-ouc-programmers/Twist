from pymongo import MongoClient
import os
from datetime import *
import json
from tweet_collector import tweet_collector
import sched
import time

with open('./collect_info.json', mode='r', encoding='utf-8') as f:
    info_arr = json.load(f)

collector = tweet_collector()

db_host = os.environ['MONGO_DB_HOST']
db_user = os.environ['MONGO_DB_USERNAME']
db_pass = os.environ['MONGO_DB_PASSWORD']
db_name = os.environ['MONGO_DB_DATABASE']


def store_tweet(hashtags, since, until):
    with MongoClient(db_host, 27017, username=db_user, password=db_pass) as client:
        tweet_db = client[db_name]
        tweet_collection = tweet_db.tweets

        tweets = collector.get_tweet(
            hashtags=hashtags, since=since, until=until)
        try:
            tweet_collection.insert_many(tweets, ordered=False)
        except:
            pass

scheduler = sched.scheduler(time.time)
for info in info_arr:

    # 感想tweet待ちの5分
    collect_time = datetime.fromisoformat(
        info['schedule']['until']) + timedelta(minutes=5)

    scheduler.enterabs(collect_time.timestamp(), 1, store_tweet, argument=(
        info['hashtags'], datetime.fromisoformat(info['schedule']['since']), collect_time))

scheduler.run()
