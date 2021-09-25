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

        auth = tweepy.OAuthHandler(self.__api_key, self.__api_secret)
        auth.set_access_token(self.__access_token, self.__access_secret)

        api = tweepy.API(auth)
        tweets = tweepy.Cursor(api.search, q=f'{" ".join(hashtags)} exclude:retweets', since=since.strftime(
            '%Y-%m-%d_%H:%M:00_JST'), until=until.strftime('%Y-%m-%d_%H:%M:00_JST'), tweet_mode='extended').items()
        for tweet in self.__limit_handled(tweets):

            tags = [tag['text'] for tag in tweet.entities['hashtags']]
            return_arr.append({
                '_id': str(tweet.id),
                'date': tweet.created_at,
                'hashtag': tags
            })
        return return_arr


if __name__ == '__main__':
    # 確認用
    with open('./collect_info.json', mode='r', encoding='utf-8') as f:
        info_arr = json.load(f)

    collector = tweet_collector()

    since = datetime.datetime.fromisoformat(info_arr[0]['schedule']['since'])
    until = datetime.datetime.fromisoformat(info_arr[0]['schedule']['until'])

    print(f'since: {since.strftime("%Y-%m-%d_%H:%M:00_JST")}')

    print(collector.get_tweet(hashtags=info_arr[0]['hashtags'], since=since, until=until))
