import os
import datetime
import tweepy
import json
import time


class tweet_collector():
    
    def __init__(self):
        self.__api_key = os.environ['TWITTER_API_KEY']
        self.__api_secret = os.environ['TWITTER_API_SECRET']
        self.__access_token = os.environ['TWITTER_ACCESS_TOKEN']
        self.__access_secret = os.environ['TWITTER_ACCESS_SECRET']

    def __limit_handled(self, cursor):
        while True:
            try:
                yield next(cursor)
            except tweepy.RateLimitError:
                time.sleep(16 * 60)
            except StopIteration:
                break

    def get_tweet(self, hashtags: list[str], since: datetime, until: datetime):
        return_arr = []

        auth = tweepy.OAuthHandler(self.api_key, self.api_secret)
        auth.set_access_token(self.access_token, self.access_secret)

        api = tweepy.API(auth)
        tweets = tweepy.Cursor(api.search, q=f'{" ".join(hashtags)} exclude:retweets', since=since.strftime(
            '%Y-%m-%d_%H:%M:00_JST'), until=until.strftime('%Y-%m-%d_%H:%M:00_JST'), tweet_mode='extended').items(1)
        for tweet in self.__limit_handled(tweets):

            tags = [tag["text"] for tag in tweet.entities["hashtags"]]
            return_arr.append({
                "id": tweet.id,
                "date": tweet.created_at,
                "hashtag": tags
            })
        return return_arr


if __name__ == "__main__":
    with open("./auth_info.json", mode="r", encoding="utf-8") as f:
        auth_info = json.load(f)

    collector = tweet_collector(
        auth_info["api_key"], auth_info["api_secret"], auth_info["access_token"], auth_info["access_secret"])
    since = datetime.datetime.fromisoformat('2021-09-23T18:00:00.000+09:00')
    until = datetime.datetime.fromisoformat('2021-09-23T19:00:00.000+09:00')

    print(f"since: {since.strftime('%Y-%m-%d_%H:%M:00_JST')}")

    print(collector.get_tweet(hashtags=["#100日後に退職する47歳"], since=since, until=until))
