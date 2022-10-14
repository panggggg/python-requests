from app.adapters.twitter_adapter import TwitterAdapter

class TwitterRepository:
    def __init__(self, twitter_adapter) -> None:
        self.twitter_adapter: TwitterAdapter = twitter_adapter
    
    def get_tweet_engagement(self, tweet_id):
        return self.twitter_adapter.get_tweet_engagement(tweet_id=tweet_id)
    
    def get_tweet_engagement_from_spider(self, tweet_id, country):
        return self.twitter_adapter.get_tweet_engagement_from_spider(tweet_id=tweet_id, country=country)
    
    def get_tweet_status(self, tweet_id):
        return self.twitter_adapter.get_tweet_status(tweet_id=tweet_id)
    
    def get_tweet_status_raw_format(self, tweet_id):
        return self.twitter_adapter.get_tweet_status_raw_format(tweet_id=tweet_id)
    
    def get_twitter_profile(self, user_id):
        return self.twitter_adapter.get_twitter_profile(user_id=user_id)
    
    def get_search_tweet(self, keyword, count):
        return self.twitter_adapter.get_search_tweet(keyword=keyword, count=count)
    
    def get_user_timeline(self, user_id, count):
        return self.twitter_adapter.get_user_timeline(user_id=user_id, count=count)
    
    def get_trend_hashtag(self, woe_id):
        return self.twitter_adapter.get_trend_hashtag(woe_id=woe_id)