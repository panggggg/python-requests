from app.repositories.instagram_repository import InstagramRepository

class InstagramUsecase:
    def __init__(self, instagram_repo) -> None:
        self.instagram_repo: InstagramRepository = instagram_repo
    
    def excute(self):
        print("""
        1. Get Instagram Locations
        2. Get Instagram Reels from account_id
        3. Get Instagram Videos from account_id
        4. Get Instagram Media Engagement with unblocker
        5. Get Instagram profile from post url
        6. Get Instagram profile from profile url with unblocker
        7. Get Instagram profile from instagram id with unblocker
        8. Get Instagram Timeline from account_id
        9. Get Instagram Comment from post url with unblocker
        10. Get Instagram Hashtag with unblocker
        """)
        instagram_request = input("Please select number of instagram request: ")
        if (instagram_request == '1'):
            print("---[ Get Instagram Locations ]---")
            location_id = input("Enter location id: ")
            return self.instagram_repo.get_instagram_location(location_id=location_id)

        if (instagram_request == '2'):
            print("---[ Get Instagram Reels from account_id ]---")
            account_id = input("Enter account id: ")
            return self.instagram_repo.get_instagram_reel_from_account_id(account_id=account_id)

        if (instagram_request == '3'):
            print("---[ Get Instagram Videos from account_id ]---")
            account_id = input("Enter account id: ")
            return self.instagram_repo.get_instagram_video_from_account_id(account_id=account_id)

        if (instagram_request == '4'):
            print("---[ Get Instagram Media Engagement with unblocker ]---")
            url = input("Enter url: ")
            return self.instagram_repo.get_instagram_media_engagement_with_unblocker(url=url)

        if (instagram_request == '5'):
            print("---[ Get Instagram profile from post url ]---")
            url = input("Enter url: ")
            return self.instagram_repo.get_instagram_profile_from_post_url(url=url)

        if (instagram_request == '6'):
            print("---[ Get Instagram profile from profile url with unblocker ]---")
            url = input("Enter url: ")
            return self.instagram_repo.get_instagram_profile_from_profile_url_with_unblocker(url=url)

        if (instagram_request == '7'):
            print("---[ Get Instagram profile from instagram id with unblocker ]---")
            user_id = input("Enter user id: ")
            return self.instagram_repo.get_instagram_profile_from_instagram_id_with_unblocker(user_id=user_id)

        if (instagram_request == '8'):
            print("---[ Get Instagram Timeline from account_id ]---")
            account_id = input("Enter account id: ")
            return self.instagram_repo.get_instagram_timeline_from_account_id(account_id=account_id)

        if (instagram_request == '9'):
            print("---[ Get Instagram Comment from post url with unblocker ]---")
            url = input("Enter url: ")
            shortcode = input("Enter shortcode: ")
            return self.instagram_repo.get_instagram_comment_from_post_url_with_unblocker(url=url, shortcode=shortcode)

        if (instagram_request == '10'):
            print("---[ Get Instagram Hashtag with unblocker ]---")
            hashtag = input("Enter hashtag: ")
            end_cursor = input("Enter endcursor: ")
            return self.instagram_repo.get_instagram_hashtag_with_unblocker(hashtag=hashtag, end_cursor=end_cursor)
