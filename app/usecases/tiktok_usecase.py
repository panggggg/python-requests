from app.repositories.tiktok_repository import TikTokRepository

class TikTokUsecase:
    def __init__(self, tiktok_repo) -> None:
        self.tiktok_repo: TikTokRepository = tiktok_repo

    def excute(self):
        print("""
        1. Get user info
        2. Get user info by user_id
        3. Get user timeline
        4. Get hashtag info
        5. Get hashtag timeline
        """)
        tiktok_request = input("Please select number [1-5] of tiktok request: ")
        if(tiktok_request == '1'):
            print("---[ Get user info ]---")
            username = input("Enter username: ")
            return self.tiktok_repo.get_user_info(username=username)

        if(tiktok_request == '2'):
            print("---[ Get user info by user_id ]---")
            user_id = input("Enter user id: ")
            return self.tiktok_repo.get_user_info_by_user_id(user_id=user_id)
            
        if(tiktok_request == '3'):
            print("---[ Get user timeline ]---")
            sec_uid = input("Enter user sec_uid: ")
            return self.tiktok_repo.get_user_timeline(sec_uid=sec_uid)

        if(tiktok_request == '4'):
            print("---[ Get hashtag info ]---")
            hashtag = input("Enter hashtag: ")
            return self.tiktok_repo.get_hashtag_info(hashtag=hashtag)

        if(tiktok_request == '5'):
            print("---[ Get hashtag timeline ]---")
            hashtag_id = input("Enter hashtag id: ")
            return self.tiktok_repo.get_hashtag_timeline(hashtag_id=hashtag_id)

        else:
            print("[Error] Please enter number 1 - 5")