from app.repositories.twitter_repository import TwitterRepository

class TwitterUsecase:
    def __init__(self, twitter_repo) -> None:
        self.twitter_repo: TwitterRepository = twitter_repo
    
    def excute(self):
        print("""
        1. Get Tweet Engagement
        2. Get Twitter Engagement from Spider
        3. Get Tweet Status
        4. Get Tweet Status Raw Format
        5. Get Twitter Profile
        6. Get Search-tweet
        7. Get User Timeline
        8. Get Trend Hashtag
        """)
        twitter_request = input("Please select number of twitter request: ")
        if (twitter_request == '1'):
            print("---[ Get Tweet Engagement ]---")
            tweet_id = input("Enter tweet id: ")
            return self.twitter_repo.get_tweet_engagement(tweet_id=tweet_id)

        if (twitter_request == '2'):
            print("---[ Get Twitter Engagement from Spider ]---")
            tweet_id = input("Enter tweet id: ")
            country = input("Enter country: ")
            return self.twitter_repo.get_tweet_engagement_from_spider(tweet_id=tweet_id, country=country)

        if (twitter_request == '3'):
            print("---[ Get Tweet Status ]---")
            tweet_id = input("Enter tweet id: ")
            return self.twitter_repo.get_tweet_status(tweet_id=tweet_id)

        if (twitter_request == '4'):
            print("---[ Get Tweet Status Raw Format ]---")
            tweet_id = input("Enter tweet id: ")
            return self.twitter_repo.get_tweet_status_raw_format(tweet_id=tweet_id)

        if (twitter_request == '5'):
            print("---[ Get Twitter Profile ]---")
            user_id = input("Enter user id: ")
            return self.twitter_repo.get_twitter_profile(user_id=user_id)

        if (twitter_request == '6'):
            print("---[ Get Search-tweet ]---")
            keyword = input("Enter keyword: ")
            count = input("Enter count: ")
            return self.twitter_repo.get_search_tweet(keyword=keyword, count=count)

        if (twitter_request == '7'):
            print("---[ Get User Timeline ]---")
            user_id = input("Enter user id: ")
            count = input("Enter count: ")
            return self.twitter_repo.get_user_timeline(user_id=user_id, count=count)

        if (twitter_request == '8'):
            print("---[ Get Trend Hashtag ]---")
            woe_id = input("Enter woe id: ")
            return self.twitter_repo.get_trend_hashtag(woe_id=woe_id)
            
