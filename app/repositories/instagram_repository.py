from app.adapters.instagram_adapter import InstagramAdapter

class InstagramRepository:
    def __init__(self, instagram_adapter) -> None:
        self.instagram_adapter: InstagramAdapter = instagram_adapter

    def get_instagram_location(self, location_id):
        return self.instagram_adapter.get_instagram_location(location_id=location_id)
    
    def get_instagram_reel_from_account_id(self, account_id):
        return self.instagram_adapter.get_instagram_reel_from_account_id(account_id=account_id)
    
    def get_instagram_video_from_account_id(self, account_id):
        return self.instagram_adapter.get_instagram_video_from_account_id(account_id=account_id)
    
    def get_instagram_media_engagement_with_unblocker(self, url):
        return self.instagram_adapter.get_instagram_media_engagement_with_unblocker(url=url)
    
    def get_instagram_profile_from_post_url(self, url):
        return self.instagram_adapter.get_instagram_profile_from_post_url(url=url)
    
    def get_instagram_profile_from_profile_url_with_unblocker(self, url):
        return self.instagram_adapter.get_instagram_profile_from_profile_url_with_unblocker(url=url)
    
    def get_instagram_profile_from_instagram_id_with_unblocker(self, user_id):
        return self.instagram_adapter.get_instagram_profile_from_instagram_id_with_unblocker(user_id=user_id)
    
    def get_instagram_timeline_from_account_id(self, account_id):
        return self.instagram_adapter.get_instagram_timeline_from_account_id(account_id=account_id)
        
    def get_instagram_comment_from_post_url_with_unblocker(self, url, shortcode):
        return self.instagram_adapter.get_instagram_comment_from_post_url_with_unblocker(url=url, shortcode=shortcode)
    
    def get_instagram_hashtag_with_unblocker(self, hashtag, end_cursor):
        return self.instagram_adapter.get_instagram_hashtag_with_unblocker(hashtag=hashtag, end_cursor=end_cursor)
