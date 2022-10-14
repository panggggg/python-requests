import requests
from app.helpers.request_time import request_time

class InstagramAdapter:
    def __init__(self, social_api_url, header) -> None:
        self.social_api_url = social_api_url
        self.header = header

    def get_instagram_location(self, location_id):
        endpoint = f'{self.social_api_url}/instagram/locations/{location_id}'
        return requests.get(url=endpoint, headers=self.header).json()

    def get_instagram_reel_from_account_id(self, account_id):
        endpoint = f'{self.social_api_url}/instagram/accounts/{account_id}/reels'
        return requests.get(url=endpoint, headers=self.header).json()

    def get_instagram_video_from_account_id(self, account_id):
        endpoint = f'{self.social_api_url}/instagram/accounts/{account_id}/videos'
        return requests.get(url=endpoint, headers=self.header).json()

    def get_instagram_media_engagement_with_unblocker(self, url):
        endpoint = f'{self.social_api_url}/instagram/post-engagement-unblocker'
        payload = {'url': url, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_instagram_profile_from_post_url(self, url):
        endpoint = f'{self.social_api_url}/facebook/instagram-oembed/get-profile-with-post'
        payload = {'url': url, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_instagram_profile_from_profile_url_with_unblocker(self, url):
        endpoint = f'{self.social_api_url}/instagram/profile-from-profile-url-unblocker'
        payload = {'url': url, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()
    
    def get_instagram_profile_from_instagram_id_with_unblocker(self, user_id):
        endpoint = f'{self.social_api_url}/instagram/profile-from-profile-url-unblocker'
        payload = {'user_id': user_id, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()
    
    def get_instagram_timeline_from_account_id(self, account_id):
        endpoint = f'{self.social_api_url}/instagram/get-timeline'
        payload = {'id': account_id, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_instagram_comment_from_post_url_with_unblocker(self, url, shortcode):
        endpoint = f'{self.social_api_url}/instagram/get-comment'
        payload = {'url': url, 'shortcode': shortcode, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_instagram_hashtag_with_unblocker(self, hashtag, end_cursor):
        endpoint = f'{self.social_api_url}/instagram/get-hashtag-proxy'
        payload = {'hashtag': hashtag, 'endCursor': end_cursor, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()