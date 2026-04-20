# -*- coding: utf-8 -*-

import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
VIDEO_URL = "https://www.googleapis.com/youtube/v3/videos"


def search_videos(query, region_code="ID", max_results=50):
    video_ids = []
    next_page_token = None

    while len(video_ids) < max_results:
        params = {
            "part": "snippet",
            "q": query,
            "type": "video",
            "maxResults": 50,
            "regionCode": region_code,
            "pageToken": next_page_token,
            "key": API_KEY,
        }

        response = requests.get(SEARCH_URL, params=params)
        data = response.json()

        for item in data.get("items", []):
            vid = item["id"]["videoId"]
            if vid not in video_ids:  # hindari duplikat
                video_ids.append(vid)

        next_page_token = data.get("nextPageToken")

        if not next_page_token:
            break

    return video_ids[:max_results]


def get_video_details(video_ids):
    results = []

    # batching (max 50 per request)
    for i in range(0, len(video_ids), 50):
        batch_ids = video_ids[i : i + 50]

        params = {
            "part": "snippet,statistics,contentDetails",
            "id": ",".join(batch_ids),
            "key": API_KEY,
        }

        response = requests.get(VIDEO_URL, params=params)
        data = response.json()

        for item in data.get("items", []):
            results.append(
                {
                    "videoId": item["id"],
                    "title": item["snippet"]["title"],
                    "channel": item["snippet"]["channelTitle"],
                    "views": int(item["statistics"].get("viewCount", 0)),
                    "likes": int(item["statistics"].get("likeCount", 0)),
                    "comments": int(item["statistics"].get("commentCount", 0)),
                    "publishedAt": item["snippet"]["publishedAt"],
                    "duration": item["contentDetails"]["duration"],
                    "region": params.get("regionCode", "Unknown"),  # optional
                }
            )

    return results


def build_dataset(query, region_code="ID", max_results=50):
    video_ids = search_videos(query, region_code, max_results)
    video_data = get_video_details(video_ids)

    return video_data
