from app.adapters.youtube_adapter import YouTubeAdapter

class YouTubeRepository:
    def __init__(self, youtube_adapter) -> None:
        self.youtube_adapter: YouTubeAdapter = youtube_adapter

    def get_youtube_video_engagement(self, video_id):
        return self.youtube_adapter.get_youtube_video_engagement(video_id=video_id)
    
    def get_youtube_video_engagement_from_spider(self, video_id, country):
        return self.youtube_adapter.get_youtube_video_engagement_from_spider(video_id=video_id, country=country)
    
    def get_youtube_profile_with_username(self, username):
        return self.youtube_adapter.get_youtube_profile_with_username(username=username)
    
    def get_youtube_profile_with_channel_id(self, channel_id):
        return self.youtube_adapter.get_youtube_profile_with_channel_id(channel_id=channel_id)
    
    def get_youtube_profile_with_custom_url(self, custom_url):
        return self.youtube_adapter.get_youtube_profile_with_custom_url(custom_url=custom_url)
    
    def get_youtube_video_profile_with_video_id(self, video_id):
        return self.youtube_adapter.get_youtube_video_profile_with_video_id(video_id=video_id)
    
    def get_youtube_video_comment_with_video_id(self, video_id):
        return self.youtube_adapter.get_youtube_video_comment_with_video_id(video_id=video_id)
    
    def get_youtube_playlist_video_with_playlist_id(self, playlist_id, next_page_token):
        return self.youtube_adapter.get_youtube_playlist_video_with_playlist_id(playlist_id=playlist_id, next_page_token=next_page_token)
    
    def get_youtube_search_video_with_channel_id(self, channel_id):
        return self.youtube_adapter.get_youtube_search_video_with_channel_id(channel_id=channel_id)
    
    def get_youtube_video_detail_from_list_of_video_id(self, video_id_list):
        return self.youtube_adapter.get_youtube_video_detail_from_list_of_video_id(video_id_list=video_id_list)
    
    def get_latest_youtube_comment(self, channel_id, next_page_token):
        return self.youtube_adapter.get_latest_youtube_comment(channel_id=channel_id, next_page_token=next_page_token)