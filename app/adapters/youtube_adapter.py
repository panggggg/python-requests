import requests
from app.helpers.request_time import request_time

class YouTubeAdapter:
    def __init__(self, social_api_url, header) -> None:
        self.social_api_url = social_api_url
        self.header = header

    def get_youtube_video_engagement(self, video_id):
        endpoint = f'{self.social_api_url}/youtube/video/engagement'
        payload = {'video_id': video_id, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, data=payload).json()

    def get_youtube_video_engagement_from_spider(self, video_id, country):
        endpoint = f'{self.social_api_url}/youtube/video/engagement/spider'
        payload = {'video_id': video_id, 'country': country.upper(),'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_youtube_profile_with_username(self, username):
        endpoint = f'{self.social_api_url}/youtube/channel/username/profile'
        payload = {'user_name': username, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_youtube_profile_with_channel_id(self, channel_id):
        endpoint = f'{self.social_api_url}/youtube/channel/id/profile'
        payload = {'channel_id': channel_id, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_youtube_profile_with_custom_url(self, custom_url):
        endpoint = f'{self.social_api_url}/youtube/channel/customurl/profile'
        payload = {'custom_url': custom_url, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_youtube_video_profile_with_video_id(self, video_id):
        endpoint = f'{self.social_api_url}/youtube/video/id/profile'
        payload = {'video_id': video_id, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_youtube_video_comment_with_video_id(self, video_id):
        endpoint = f'{self.social_api_url}/youtube/video/comment'
        payload = {'video_id': video_id, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()
    
    def get_youtube_playlist_video_with_playlist_id(self, playlist_id, next_page_token):
        endpoint = f'{self.social_api_url}/youtube/video/comment'
        payload = {'playlist_id': playlist_id, 'next_page_token': next_page_token, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_youtube_search_video_with_channel_id(self, channel_id):
        endpoint = f'{self.social_api_url}/youtube/videos/search'
        payload = {'channel_id': channel_id, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_youtube_video_detail_from_list_of_video_id(self, video_id_list):
        endpoint = f'{self.social_api_url}/youtube/video/list/detail'
        payload = {'video_id_list': video_id_list, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_latest_youtube_comment(self, channel_id, next_page_token):
        endpoint = f'{self.social_api_url}/youtube/channel/comment/all'
        payload = {'channel_id': channel_id, 'next_page_token': next_page_token, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()