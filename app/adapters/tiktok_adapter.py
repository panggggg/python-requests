import requests
from app.helpers.method import request_method

class TikTokAdapter:

    def __init__(self, social_api_url, header) -> None:
        self.social_api_url = social_api_url
        self.header = header
    
    def get_user_info(self, username):
        data = {
            "method": "GET",
            "endpoint": f'{self.social_api_url}/tiktok/users/{username}',
            "header": self.header,
            "payload": None
        }
        return request_method(data=data)

    def get_user_info_by_user_id(self, user_id):
        data = {
            "method": "GET",
            "endpoint": f'{self.social_api_url}/tiktok/{user_id}',
            "header": self.header,
            "payload": None
        }
        return request_method(data=data)

    def get_user_timeline(self, sec_uid):
        data = {
            "method": "GET",
            "endpoint": f'{self.social_api_url}/tiktok/users/{sec_uid}/videos',
            "header": self.header,
            "payload": None
        }
        return request_method(data=data)

    def get_hashtag_info(self, hashtag):
        data = {
            "method": "GET",
            "endpoint": f'{self.social_api_url}/tiktok/hashtags/{hashtag}',
            "header": self.header,
            "payload": None
        }
        return request_method(data=data)

    def get_hashtag_timeline(self, hashtag_id):
        endpoint = f'{self.social_api_url}/tiktok/hashtags/{hashtag_id}/videos'
        return requests.get(url=endpoint, headers=self.header, params={'cursor': 30}).json() # get with params