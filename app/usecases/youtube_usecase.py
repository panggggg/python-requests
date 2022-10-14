from app.repositories.youtube_repository import YouTubeRepository

class YouTubeUsecase:
    def __init__(self, youtube_repo) -> None:
        self.youtube_repo: YouTubeRepository = youtube_repo
    
    def excute(self):
        print("""
        1. Get Youtube Video Engagement
        2. Get Youtube Video Engagement from Spider
        3. Get YouTube Profile with username
        4. Get YouTube Profile with id channel
        5. Get YouTube Profile with custom url
        6. Get YouTube Video Profile with video id
        7. Get YouTube Video Comments with video id
        8. Get YouTube Playlist Video with Playlist ID
        9. Get YouTube Search Video with Channel ID
        10. Get YouTube video detail from list of video id
        11. Get latest YouTube comments from channel and all videos
        """)
        youtube_request = input("Please select number of youtube request: ")
        if (youtube_request == '1'):
            print("---[ Get Youtube Video Engagement ]---")
            video_id = input("Enter video id: ")
            return self.youtube_repo.get_youtube_video_engagement(video_id=video_id)

        if (youtube_request == '2'):
            print("---[ Get Youtube Video Engagement from Spider ]---")
            video_id = input("Enter video id: ")
            country = input("Enter country: ")
            return self.youtube_repo.get_youtube_video_engagement_from_spider(video_id=video_id, country=country)

        if (youtube_request == '3'):
            print("---[ Get YouTube Profile with username ]---")
            username = input("Enter username: ")
            return self.youtube_repo.get_youtube_profile_with_username(username=username)

        if (youtube_request == '4'):
            print("---[ Get YouTube Profile with id channel ]---")
            channel_id = input("Enter channel id: ")
            return self.youtube_repo.get_youtube_profile_with_channel_id(channel_id=channel_id)

        if (youtube_request == '5'):
            print("---[ Get YouTube Profile with custom url ]---")
            custom_url = input("Enter custom url: ")
            return self.youtube_repo.get_youtube_profile_with_custom_url(custom_url=custom_url)

        if (youtube_request == '6'):
            print("---[ Get YouTube Video Profile with video id ]---")
            video_id = input("Enter video id: ")
            return self.youtube_repo.get_youtube_video_profile_with_video_id(video_id=video_id)

        if (youtube_request == '7'):
            print("---[ Get YouTube Video Comments with video id ]---")
            video_id = input("Enter video id: ")
            return self.youtube_repo.get_youtube_video_comment_with_video_id(video_id=video_id)

        if (youtube_request == '8'):
            print("---[ Get YouTube Playlist Video with Playlist ID ]---")
            playlist_id = input("Enter video id: ")
            next_page_token = input("Enter next page token: ")
            return self.youtube_repo.get_youtube_playlist_video_with_playlist_id(playlist_id=playlist_id, next_page_token=next_page_token)

        if (youtube_request == '9'):
            print("---[ Get YouTube Search Video with Channel ID ]---")
            channel_id = input("Enter channel id: ")
            return self.youtube_repo.get_youtube_search_video_with_channel_id(channel_id=channel_id)

        if (youtube_request == '10'):
            print("---[ Get YouTube video detail from list of video id ]---")
            video_id_list = input("Enter video id list: ")
            return self.youtube_repo.get_youtube_video_detail_from_list_of_video_id(video_id_list=video_id_list)

        if (youtube_request == '11'):
            print("---[ Get latest YouTube comments from channel and all videos ]---")
            channel_id = input("Enter channel id: ")
            next_page_token = input("Enter next page token: ")
            return self.youtube_repo.get_latest_youtube_comment(channel_id=channel_id, next_page_token=next_page_token)
