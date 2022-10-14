import requests
from app.helpers.request_time import request_time

class FacebookAdapter:
    def __init__(self, social_api_url, header) -> None:
        self.social_api_url = social_api_url
        self.header = header

    def get_facebook_share_on_link(self, link):
        endpoint = f'{self.social_api_url}/facebook/share-on-link'
        payload = {'link': link, 'request_time': request_time()}
        return requests.request("POST", url=endpoint, headers=self.header, data=payload).json()
    
    def get_facebook_scrape_on_link(self, link):
        endpoint = f'{self.social_api_url}/facebook/scrape-on-link'
        payload = {'link': link, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_facebook_page_album(self, page_id, limit):
        data = ["content", "engagement"]
        endpoint = f'{self.social_api_url}/facebook/page-albums'
        payload = {'page_id': page_id, 'limit': limit, 'data': data, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_facebook_albums_info(self, album_id):
        endpoint = f'{self.social_api_url}/facebook/albums-info'
        payload = {'albums_id': album_id, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_facebook_page_feed(self, page_id, limit):
        endpoint = f'{self.social_api_url}/facebook/page-feed'
        payload = {'page_id': page_id, 'limit': limit, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_facebook_page_post(self, post_id):
        endpoint = f'{self.social_api_url}/facebook/page-post'
        payload = {'post_id': post_id, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_facebook_page_photo(self, photo_id):
        endpoint = f'{self.social_api_url}/facebook/page-photo'
        payload = {'photo_id': photo_id, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_facebook_page_profile(self, page_id):
        endpoint = f'{self.social_api_url}/facebook/page-profile'
        payload = {'page_id': page_id, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_facebook_page_comment(self, post_id, limit):
        data = ["content", "engagement"]
        endpoint = f'{self.social_api_url}/facebook/post-comments'
        payload = {'post_id': post_id, 'limit': limit, 'data': data, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_facebook_post_engagement(self, post_id):
        endpoint = f'{self.social_api_url}/facebook/post-engagement'
        payload = {'post_id': post_id, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_instagram_oembed_profile_with_post(self, url):
        endpoint = f'{self.social_api_url}/facebook/instagram-oembed/get-profile-with-post'
        payload = {'url': url, 'request_time': request_time()}
        return requests.post(url=endpoint, headers=self.header, json=payload).json()

    def get_instagram_oembed_with_post(self, post_url):
        endpoint = f'{self.social_api_url}/facebook/instagram-oembed'
        return requests.get(url=endpoint, headers=self.header, params=[('post_url', post_url)]).json()