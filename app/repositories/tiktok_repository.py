from app.adapters.tiktok_adapter import TikTokAdapter

class TikTokRepository:
    def __init__(self, tiktok_adapter) -> None:
        self.tiktok_adapter = tiktok_adapter

    def get_user_info(self, username):
        return self.tiktok_adapter.get_user_info(username=username)

    def get_user_info_by_user_id(self, user_id):
        return self.tiktok_adapter.get_user_info_by_user_id(user_id=user_id)

    def get_user_timeline(self, sec_uid):
        return self.tiktok_adapter.get_user_timeline(sec_uid=sec_uid)

    def get_hashtag_info(self, hashtag):
        return self.tiktok_adapter.get_hashtag_info(hashtag=hashtag)

    def get_hashtag_timeline(self, hashtag_id):
        return self.tiktok_adapter.get_hashtag_timeline(hashtag_id=hashtag_id)