from app.adapters.facebook_adapter import FacebookAdapter

class FacebookRepository:
    def __init__(self, facebook_adapter) -> None:
        self.facebook_adapter = facebook_adapter

    def get_facebook_share_on_link(self, link):
        return self.facebook_adapter.get_facebook_share_on_link(link=link)

    def get_facebook_scrape_on_link(self, link):
        return self.facebook_adapter.get_facebook_scrape_on_link(link=link)

    def get_facebook_page_album(self, page_id, limit):
        return self.facebook_adapter.get_facebook_page_album(page_id=page_id, limit=limit)

    def get_facebook_albums_info(self, album_id):
        return self.facebook_adapter.get_facebook_albums_info(album_id=album_id)

    def get_facebook_page_feed(self, page_id, limit):
        return self.facebook_adapter.get_facebook_page_feed(page_id=page_id, limit=limit)

    def get_facebook_page_post(self, post_id):
        return self.facebook_adapter.get_facebook_page_post(post_id=post_id)
    
    def get_facebook_page_photo(self, photo_id):
        return self.facebook_adapter.get_facebook_page_photo(photo_id=photo_id)
    
    def get_facebook_page_profile(self, page_id):
        return self.facebook_adapter.get_facebook_page_profile(page_id=page_id)
    
    def get_facebook_page_comment(self, post_id, limit):
        return self.facebook_adapter.get_facebook_page_comment(post_id=post_id, limit=limit)
    
    def get_facebook_post_engagement(self, post_id):
        return self.facebook_adapter.get_facebook_post_engagement(post_id=post_id)
    
    def get_instagram_oembed_profile_with_post(self, url):
        return self.facebook_adapter.get_instagram_oembed_profile_with_post(url=url)
    
    def get_instagram_oembed_with_post(self, post_url):
        return self.facebook_adapter.get_instagram_oembed_with_post(post_url=post_url)
    