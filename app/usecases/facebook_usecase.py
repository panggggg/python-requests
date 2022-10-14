from app.repositories.facebook_repository import FacebookRepository

class FacebookUsecase:
    def __init__(self, facebook_repo) -> None:
        self.facebook_repo: FacebookRepository = facebook_repo

    def excute(self):
        print("""
        1. Get Facebook share on link
        2. Get Facebook Scrape On Link
        3. Get Facebook Page Albums
        4. Get Facebook Albums Info
        5. Get facebook Page Feed
        6. Get facebook Page Post
        7. Get Facebook Page Photo
        8. Get facebook Page Profile
        9. Get Facebook Post Comment
        10. Get Facebook Post Engagement
        11. Get Instagram Oembed Profile With Post
        12. Get Instagram Oembed With Post

        """)
        facebook_request = input("Please select number of facebook request: ")
        if (facebook_request == '1'):
            print("---[ Get Facebook share on link ]---")
            link = input("Enter link: ")
            return self.facebook_repo.get_facebook_share_on_link(link=link)

        if (facebook_request == '2'):
            print("---[ Get Facebook Scrape On Link ]---")
            link = input("Enter link: ")
            return self.facebook_repo.get_facebook_scrape_on_link(link=link)

        if (facebook_request == '3'):
            print("---[ Get Facebook Page Albums ]---")
            page_id = input("Enter page id: ")
            limit = input("Enter limit: ")
            return self.facebook_repo.get_facebook_page_album(page_id=page_id, limit=limit)

        if (facebook_request == '4'):
            print("---[ Get Facebook Albums Info ]---")
            album_id = input("Enter albums id: ")
            return self.facebook_repo.get_facebook_albums_info(album_id=album_id)

        if (facebook_request == '5'):
            print("---[ Get facebook Page Feed ]---")
            page_id = input("Enter page id: ")
            limit = input("Enter limit: ")
            return self.facebook_repo.get_facebook_page_feed(page_id=page_id, limit=limit)

        if (facebook_request == '6'):
            print("---[ Get facebook Page Post ]---")
            post_id = input("Enter post id: ")
            return self.facebook_repo.get_facebook_page_post(post_id=post_id)

        if (facebook_request == '7'):
            print("---[ Get facebook Page Photo ]---")
            photo_id = input("Enter photo id: ")
            return self.facebook_repo.get_facebook_page_photo(photo_id=photo_id)

        if (facebook_request == '8'):
            print("---[ Get facebook Page Profile ]---")
            page_id = input("Enter page id: ")
            return self.facebook_repo.get_facebook_page_profile(page_id=page_id)

        if (facebook_request == '9'):
            print("---[ Get Facebook Page Comment ]---")
            post_id = input("Enter post id: ")
            limit = input("Enter limit: ")
            return self.facebook_repo.get_facebook_page_comment(post_id=post_id, limit=limit)

        if (facebook_request == '10'):
            print("---[ Get Facebook Post Engagement ]---")
            post_id = input("Enter post id: ")
            return self.facebook_repo.get_facebook_post_engagement(post_id=post_id)

        if (facebook_request == '11'):
            print("---[ Get Instagram Oembed Profile With Post ]---")
            url = input("Enter url: ")
            return self.facebook_repo.get_instagram_oembed_profile_with_post(url=url)

        if (facebook_request == '12'):
            print("---[ Get Instagram Oembed With Post ]---")
            post_url = input("Enter post url: ")
            return self.facebook_repo.get_instagram_oembed_with_post(post_url=post_url)
            
        else:
            print("[Error] Please enter number 1 - 12")