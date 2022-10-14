import requests
from app.helpers.request_time import request_time

class TwitterAdapter:
    def __init__(self, social_api_url, header) -> None:
        self.social_api_url = social_api_url
        self.header = header

    def get_tweet_engagement(self, tweet_id):
        endpoint = f'{self.social_api_url}/twitter/tweet-engagement'
        payload = {'tweet_id': tweet_id, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()
    
    def get_tweet_engagement_from_spider(self, tweet_id, country):
        endpoint = f'{self.social_api_url}/twitter/tweet-engagement-spider'
        payload = {'id': tweet_id, 'country': country.upper()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_tweet_status(self, tweet_id):
        endpoint = f'{self.social_api_url}/twitter/tweet-status'
        payload = {'tweet_id': tweet_id, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()
    
    def get_tweet_status_raw_format(self, tweet_id):
        endpoint = f'{self.social_api_url}/twitter/tweet-status-raw'
        payload = {'tweet_id': tweet_id, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_twitter_profile(self, user_id):
        endpoint = f'{self.social_api_url}/twitter/profile'
        payload = {'user_id': user_id, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_search_tweet(self, keyword, count):
        endpoint = f'{self.social_api_url}/twitter/search-tweet'
        payload = {'keyword': keyword, 'count': count, "exclude_retweet": False, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_user_timeline(self, user_id, count):
        endpoint = f'{self.social_api_url}/twitter/user-timeline'
        payload = {'user_id': user_id, 'count': count, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_trend_hashtag(self, woe_id):
        endpoint = f'{self.social_api_url}/twitter/trend'
        payload = {'woe_id': woe_id, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()