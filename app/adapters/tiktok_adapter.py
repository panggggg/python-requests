import requests

class TikTokAdapter:

    def __init__(self, social_api_url, header) -> None:
        self.social_api_url = social_api_url
        self.header = header
    
    def get_user_info(self, username):
        endpoint = f'{self.social_api_url}/tiktok/users/{username}'
        return requests.get(url=endpoint, headers=self.header).json()

    def get_user_info_by_user_id(self, user_id):
        endpoint = f'{self.social_api_url}/tiktok/{user_id}'
        return requests.get(url=endpoint, headers=self.header).json()

    def get_user_timeline(self, sec_uid):
        endpoint = f'{self.social_api_url}/tiktok/users/{sec_uid}/videos'
        return requests.get(url=endpoint, headers=self.header).json()

    def get_hashtag_info(self, hashtag):
        endpoint = f'{self.social_api_url}/tiktok/hashtags/{hashtag}'
        return requests.get(url=endpoint, headers=self.header).json()

    def get_hashtag_timeline(self, hashtag_id):
        endpoint = f'{self.social_api_url}/tiktok/hashtags/{hashtag_id}/videos'
        return requests.get(url=endpoint, headers=self.header, params={'cursor': 30}).json() # get with params