import fire
import requests
from request_time import request_time

social_api_url = "https://social-api.wisesight.dev"
heads = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZXJ2aWNlIjoic29jaWFsLWFwaSIsImlhdCI6MTUyNjg3ODExNn0.ortjsdqjSyQhOnVE0v67MLwnOXZLFMtL1fqtJcqKpQE"}


# instagram = requests.get(f'{social_api_url}/instagram/locations/106947657857917', headers=heads)
# print(instagram.json())

def social_api(channel):
    print("Channel: ", channel)
    if (channel == "tiktok"):
        tiktok()
    if (channel == 'facebook'):
        facebook()
    if (channel == 'pantip'):
        pantip()
    if (channel == 'twitter'):
        twitter()
    if (channel == 'youtube'):
        youtube()
    if (channel == 'instagram'):
        instagram()

def tiktok():
    data_type = input("What type do you want? [user, hashtag]: ")
    if(data_type == "user"):
        user_type = input("What user type? [info, timeline]: ")
        if (user_type == "info"):
            param = input("Enter username or user id: ")
            if (param.isdigit()):
                endpoint = f'{social_api_url}/tiktok/{param}'
                print(endpoint)
                res = requests.get(url=endpoint, headers=heads)
                print(res.json())
            else:
                endpoint = f'{social_api_url}/tiktok/users/{param}'
                res = requests.get(url=endpoint, headers=heads)
                print(res.json())
        elif (user_type == "timeline"):
            sec_uid = input("Enter user sec_uid: ")
            endpoint = f'{social_api_url}/tiktok/users/{sec_uid}/videos'
            res = requests.get(url=endpoint, headers=heads)
            print(res.json())
    elif(data_type == "hashtag"):
        user_type = input("What user type? [info, timeline]: ")
        if (user_type == "info"):
            hashtag = input("Enter hashtag: ")
            endpoint = f'{social_api_url}/tiktok/hashtags/{hashtag}'
            res = requests.get(url=endpoint, headers=heads)
            print(res.json())
        if (user_type == "timeline"):
            hashtag_id = input("Enter hashtag id: ")
            endpoint = f'{social_api_url}/tiktok/hashtags/{hashtag_id}/videos?cursor=30'
            res = requests.get(url=endpoint, headers=heads)
            print(res.json())
    else:
        print("Only have user or hashtag!")
    
def facebook():
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
        endpoint = f'{social_api_url}/facebook/share-on-link'
        payload = {'link': link, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (facebook_request == '2'):
        print("---[ Get Facebook Scrape On Link ]---")
        link = input("Enter link: ")
        endpoint = f'{social_api_url}/facebook/scrape-on-link'
        payload = {'link': link, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (facebook_request == '3'):
        print("---[ Get Facebook Page Albums ]---")
        page_id = input("Enter page id: ")
        limit = input("Enter limit: ")
        data = ["content", "engagement"]
        endpoint = f'{social_api_url}/facebook/page-albums'
        payload = {'page_id': page_id, 'limit': limit, 'data': data, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (facebook_request == '4'):
        print("---[ Get Facebook Albums Info ]---")
        albums_id = input("Enter albums id: ")
        endpoint = f'{social_api_url}/facebook/albums-info'
        payload = {'albums_id': albums_id, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (facebook_request == '5'):
        print("---[ Get facebook Page Feed ]---")
        page_id = input("Enter page id: ")
        limit = input("Enter limit: ")
        endpoint = f'{social_api_url}/facebook/page-feed'
        payload = {'page_id': page_id, 'limit': limit, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (facebook_request == '6'):
        print("---[ Get facebook Page Post ]---")
        post_id = input("Enter post id: ")
        endpoint = f'{social_api_url}/facebook/page-post'
        payload = {'post_id': post_id, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (facebook_request == '7'):
        print("---[ Get facebook Page Photo ]---")
        photo_id = input("Enter photo id: ")
        endpoint = f'{social_api_url}/facebook/page-photo'
        payload = {'photo_id': photo_id, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (facebook_request == '8'):
        print("---[ Get facebook Page Profile ]---")
        page_id = input("Enter page id: ")
        endpoint = f'{social_api_url}/facebook/page-profile'
        payload = {'page_id': page_id, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (facebook_request == '9'):
        print("---[ Get Facebook Page Comment ]---")
        post_id = input("Enter post id: ")
        limit = input("Enter limit: ")
        data = ["content", "engagement"]
        endpoint = f'{social_api_url}/facebook/post-comments'
        payload = {'post_id': post_id, 'limit': limit, 'data': data, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (facebook_request == '10'):
        print("---[ Get Facebook Post Engagement ]---")
        post_id = input("Enter post id: ")
        endpoint = f'{social_api_url}/facebook/post-engagement'
        payload = {'post_id': post_id, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (facebook_request == '11'):
        print("---[ Get Instagram Oembed Profile With Post ]---")
        url = input("Enter url: ")
        endpoint = f'{social_api_url}/facebook/instagram-oembed/get-profile-with-post'
        payload = {'url': url, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (facebook_request == '12'):
        print("---[ Get Instagram Oembed With Post ]---")
        post_url = input("Enter post url: ")
        endpoint = f'{social_api_url}/facebook/instagram-oembed?post_url={post_url}'
        res = requests.get(url=endpoint, headers=heads)
        print(res.json())
    else:
        print("[Error] Please enter number 1 - 12")

def pantip():
    print("""
        1. Get Pantip Topic Info
        2. Get Pantip Topic By room
        3. Get Pantip Topic By tag
    """)
    pantip_request = input("Please select number of pantip request: ")
    if (pantip_request == '1'):
        print("---[ Get Pantip Topic Info ]---")
        topic_id = input("Enter topic id: ")
        endpoint = f'{social_api_url}/pantip/topic-engagement'
        payload = {'topic_id': topic_id, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (pantip_request == '2'):
        print("---[ Get Pantip Topic By room ]---")
        room = input("Enter room: ")
        tid = input("Enter tid: ")
        endpoint = f'{social_api_url}/pantip/topic-by-room'
        payload = {'room': room, 'tid': tid, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (pantip_request == '3'):
        print("---[ Get Pantip Topic By tag ]---")
        tag = input("Enter tag: ")
        tid = input("Enter tid: ")
        endpoint = f'{social_api_url}/pantip/topic-by-tag'
        payload = {'tag': tag, 'tid': tid, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())

def twitter():
    print("""
        1. Get Tweet Engagement
        2. Get Twitter Engagement from Spider
        3. Get Twitter Engagement from Spider of tweet without quote and reply count
        4. Get Tweet Status
        5. Get Tweet Status Raw Format
        6. Get Twitter Profile
        7. Get Search-tweet
        8. Get User Timeline
        9. Get Trend Hashtag
    """)
    twitter_request = input("Please select number of twitter request: ")
    if (twitter_request == '1'):
        print("---[ Get Tweet Engagement ]---")
        tweet_id = input("Enter tweet id: ")
        endpoint = f'{social_api_url}/twitter/tweet-engagement'
        payload = {'tweet_id': tweet_id, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (twitter_request == '2'):
        print("---[ Get Twitter Engagement from Spider ]---")
        id = input("Enter id: ")
        country = input("Enter country: ")
        endpoint = f'{social_api_url}/twitter/tweet-engagement-spider'
        payload = {'id': id, 'country': country.upper()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (twitter_request == '3'):
        print("---[ Get Twitter Engagement from Spider of tweet without quote and reply count ]---")
        id = input("Enter id: ")
        country = input("Enter country: ")
        endpoint = f'{social_api_url}/twitter/tweet-engagement-spider'
        payload = {'id': id, 'country': country.upper()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (twitter_request == '4'):
        print("---[ Get Tweet Status ]---")
        tweet_id = input("Enter tweet id: ")
        endpoint = f'{social_api_url}/twitter/tweet-status'
        payload = {'tweet_id': tweet_id, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (twitter_request == '5'):
        print("---[ Get Tweet Status Raw Format ]---")
        tweet_id = input("Enter tweet id: ")
        endpoint = f'{social_api_url}/twitter/tweet-status-raw'
        payload = {'tweet_id': tweet_id, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (twitter_request == '6'):
        print("---[ Get Twitter Profile ]---")
        user_id = input("Enter user id: ")
        endpoint = f'{social_api_url}/twitter/profile'
        payload = {'user_id': user_id, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (twitter_request == '7'):
        print("---[ Get Search-tweet ]---")
        keyword = input("Enter keyword: ")
        count = input("Enter count: ")
        endpoint = f'{social_api_url}/twitter/search-tweet'
        payload = {'keyword': keyword, 'count': count, "exclude_retweet": False, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (twitter_request == '8'):
        print("---[ Get User Timeline ]---")
        user_id = input("Enter user id: ")
        count = input("Enter count: ")
        endpoint = f'{social_api_url}/twitter/user-timeline'
        payload = {'user_id': user_id, 'count': count, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (twitter_request == '9'):
        print("---[ Get Trend Hashtag ]---")
        woe_id = input("Enter woe id: ")
        endpoint = f'{social_api_url}/twitter/trend'
        payload = {'woe_id': woe_id, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())

def youtube():
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
        10. Get YouTube Playlist Video with Playlist ID with nextPageToken
        11. Get YouTube video detail from list of video id
        12. Get latest YouTube comments from channel and all videos
    """)
    youtube_request = input("Please select number of youtube request: ")
    if (youtube_request == '1'):
        print("---[ Get Youtube Video Engagement ]---")
        video_id = input("Enter video id: ")
        endpoint = f'{social_api_url}/youtube/video/engagement'
        payload = {'video_id': video_id, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (youtube_request == '2'):
        print("---[ Get Youtube Video Engagement from Spider ]---")
        video_id = input("Enter video id: ")
        country = input("Enter country: ")
        endpoint = f'{social_api_url}/youtube/video/engagement/spider'
        payload = {'video_id': video_id, 'country': country.upper(),'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (youtube_request == '3'):
        print("---[ Get YouTube Profile with username ]---")
        user_name = input("Enter user name: ")
        endpoint = f'{social_api_url}/youtube/channel/username/profile'
        payload = {'user_name': user_name, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (youtube_request == '4'):
        print("---[ Get YouTube Profile with id channel ]---")
        channel_id = input("Enter channel id: ")
        endpoint = f'{social_api_url}/youtube/channel/id/profile'
        payload = {'channel_id': channel_id, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (youtube_request == '5'):
        print("---[ Get YouTube Profile with custom url ]---")
        custom_url = input("Enter custom url: ")
        endpoint = f'{social_api_url}/youtube/channel/customurl/profile'
        payload = {'custom_url': custom_url, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (youtube_request == '6'):
        print("---[ Get YouTube Video Profile with video id ]---")
        video_id = input("Enter video id: ")
        endpoint = f'{social_api_url}/youtube/video/id/profile'
        payload = {'video_id': video_id, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (youtube_request == '7'):
        print("---[ Get YouTube Video Comments with video id ]---")
        video_id = input("Enter video id: ")
        endpoint = f'{social_api_url}/youtube/video/comment'
        payload = {'video_id': video_id, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (youtube_request == '8'):
        print("---[ Get YouTube Playlist Video with Playlist ID ]---")
        video_id = input("Enter video id: ")
        endpoint = f'{social_api_url}/youtube/video/comment'
        payload = {'video_id': video_id, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (youtube_request == '9'):
        print("---[ Get YouTube Search Video with Channel ID ]---")
        channel_id = input("Enter channel id: ")
        endpoint = f'{social_api_url}/youtube/videos/search'
        payload = {'channel_id': channel_id, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (youtube_request == '10'):
        print("---[ Get YouTube Playlist Video with Playlist ID with nextPageToken ]---")
        playlist_id = input("Enter playlist id: ")
        next_page_token = input("Enter next page token: ")
        endpoint = f'{social_api_url}/youtube/playlist/video'
        payload = {'playlist_id': playlist_id, 'next_page_token': next_page_token, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (youtube_request == '11'):
        print("---[ Get YouTube video detail from list of video id ]---")
        video_id_list = input("Enter video id list: ")
        endpoint = f'{social_api_url}/youtube/video/list/detail'
        payload = {'video_id_list': video_id_list, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (youtube_request == '12'):
        print("---[ Get latest YouTube comments from channel and all videos ]---")
        channel_id = input("Enter channel id: ")
        next_page_token = input("Enter next page token: ")
        endpoint = f'{social_api_url}/youtube/channel/comment/all'
        payload = {'channel_id': channel_id, 'next_page_token': next_page_token, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())

def instagram():
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
        endpoint = f'{social_api_url}/instagram/locations/{location_id}'
        res = requests.get(url=endpoint, headers=heads)
        print(res.json())
    if (instagram_request == '2'):
        print("---[ Get Instagram Reels from account_id ]---")
        account_id = input("Enter account id: ")
        endpoint = f'{social_api_url}/instagram/accounts/{account_id}/reels'
        res = requests.get(url=endpoint, headers=heads)
        print(res.json())
    if (instagram_request == '3'):
        print("---[ Get Instagram Videos from account_id ]---")
        account_id = input("Enter account id: ")
        endpoint = f'{social_api_url}/instagram/accounts/{account_id}/videos'
        res = requests.get(url=endpoint, headers=heads)
        print(res.json())
    if (instagram_request == '4'):
        print("---[ Get Instagram Media Engagement with unblocker ]---")
        url = input("Enter url: ")
        endpoint = f'{social_api_url}/instagram/post-engagement-unblocker'
        payload = {'url': url, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (instagram_request == '5'):
        print("---[ Get Instagram profile from post url ]---")
        url = input("Enter url: ")
        endpoint = f'{social_api_url}/facebook/instagram-oembed/get-profile-with-post'
        payload = {'url': url, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (instagram_request == '6'):
        print("---[ Get Instagram profile from profile url with unblockerl ]---")
        url = input("Enter url: ")
        endpoint = f'{social_api_url}/instagram/profile-from-profile-url-unblocker'
        payload = {'url': url, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (instagram_request == '7'):
        print("---[ Get Instagram profile from instagram id with unblocker ]---")
        user_id = input("Enter user id: ")
        endpoint = f'{social_api_url}/instagram/profile-from-profile-url-unblocker'
        payload = {'user_id': user_id, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (instagram_request == '8'):
        print("---[ Get Instagram Timeline from account_id ]---")
        account_id = input("Enter account id: ")
        endpoint = f'{social_api_url}/instagram/get-timeline'
        payload = {'id': account_id, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (instagram_request == '9'):
        print("---[ Get Instagram profile from profile url with unblockerl ]---")
        url = input("Enter url: ")
        shotcode = input("Enter shortcode: ")
        endpoint = f'{social_api_url}/instagram/get-comment'
        payload = {'url': url, 'shortcode': shotcode, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())
    if (instagram_request == '10'):
        print("---[ Get Instagram Timeline from account_id ]---")
        hashtag = input("Enter hashtag: ")
        end_cursor = input("Enter endcursor: ")
        endpoint = f'{social_api_url}/instagram/get-timeline'
        payload = {'hashtag': hashtag, 'endCursor': end_cursor, 'request_time': request_time()}
        res = requests.post(url=endpoint, headers=heads, json=payload)
        print(res.json())

if __name__ == '__main__':
    fire.Fire(social_api)