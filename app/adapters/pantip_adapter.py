import requests
from app.helpers.request_time import request_time

class PantipAdapter:
    def __init__(self, social_api_url, header) -> None:
        self.social_api_url = social_api_url
        self.header = header

    def get_pantip_topic_info(self, topic_id):
        endpoint = f'{self.social_api_url}/pantip/topic-engagement'
        payload = {'topic_id': topic_id, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_pantip_topic_by_room(self, tid, room):
        endpoint = f'{self.social_api_url}/pantip/topic-by-room'
        payload = {'room': room, 'tid': tid, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_pantip_topic_by_tag(self, tid, tag):
        endpoint = f'{self.social_api_url}/pantip/topic-by-tag'
        payload = {'tag': tag, 'tid': tid, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()