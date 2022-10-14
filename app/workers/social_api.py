import fire
import os
import sys

module_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(module_path + "/../../")

from app.repositories.tiktok_repository import TikTokRepository
from app.adapters.tiktok_adapter import TikTokAdapter
from app.usecases.tiktok_usecase import TikTokUsecase

from app.repositories.facebook_repository import FacebookRepository
from app.adapters.facebook_adapter import FacebookAdapter
from app.usecases.facebook_usecase import FacebookUsecase

from app.adapters.pantip_adapter import PantipAdapter
from app.repositories.pantip_repository import PantipRepository
from app.usecases.pantip_usecase import PantipUsecase

from app.adapters.twitter_adapter import TwitterAdapter
from app.repositories.twitter_repository import TwitterRepository
from app.usecases.twitter_usecase import TwitterUsecase

from app.adapters.youtube_adapter import YouTubeAdapter
from app.repositories.youtube_repository import YouTubeRepository
from app.usecases.youtube_usecase import YouTubeUsecase

from app.adapters.instagram_adapter import InstagramAdapter
from app.repositories.instagram_repository import InstagramRepository
from app.usecases.instagram_usecase import InstagramUsecase

class Command:
    def run(channel: str):
        print("Channel: ", channel)
        social_api_url = "https://social-api.wisesight.dev"
        header = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZXJ2aWNlIjoic29jaWFsLWFwaSIsImlhdCI6MTUyNjg3ODExNn0.ortjsdqjSyQhOnVE0v67MLwnOXZLFMtL1fqtJcqKpQE"}
        try:
            if (channel == "tiktok"):
                tiktok_adapter = TikTokAdapter(social_api_url=social_api_url, header=header)
                tiktok_repo = TikTokRepository(tiktok_adapter=tiktok_adapter)
                tiktok_usecase = TikTokUsecase(tiktok_repo=tiktok_repo)
                return tiktok_usecase.excute()

            if (channel == 'facebook'):
                facebook_adapter = FacebookAdapter(social_api_url=social_api_url, header=header)
                facebook_repo = FacebookRepository(facebook_adapter=facebook_adapter)
                facebook_usecase = FacebookUsecase(facebook_repo=facebook_repo)
                return facebook_usecase.excute()

            if (channel == 'pantip'):
                pantip_adapter = PantipAdapter(social_api_url=social_api_url, header=header)
                pantip_repo = PantipRepository(pantip_adapter=pantip_adapter)
                pantip_usecase = PantipUsecase(pantip_repo=pantip_repo)
                return pantip_usecase.excute()

            if (channel == 'twitter'):
                twitter_adapter = TwitterAdapter(social_api_url=social_api_url, header=header)
                twitter_repo = TwitterRepository(twitter_adapter=twitter_adapter)
                twitter_usecase = TwitterUsecase(twitter_repo=twitter_repo)
                return twitter_usecase.excute()

            if (channel == 'youtube'):
                youtube_adapter = YouTubeAdapter(social_api_url=social_api_url, header=header)
                youtube_repo = YouTubeRepository(youtube_adapter=youtube_adapter)
                youtube_usecase = YouTubeUsecase(youtube_repo=youtube_repo)
                return youtube_usecase.excute()

            if (channel == 'instagram'):
                instagram_adapter = InstagramAdapter(social_api_url=social_api_url, header=header)
                instagram_repo = InstagramRepository(instagram_adapter=instagram_adapter)
                instagram_usecase = InstagramUsecase(instagram_repo=instagram_repo)
                return instagram_usecase.excute()
            else:
                print("[ERROR] Please enter channel only: [facebook, instagram, tiktok, pantip, youtube, twitter]")
        except KeyboardInterrupt:
            print("Exit")

    if __name__ == '__main__':
        fire.Fire(run)