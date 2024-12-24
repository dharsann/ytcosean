from googleapiclient.discovery import build
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
import os

api_key = os.getenv("API_KEY")

def get_video_comments(video_id, api_key):
    youtube = build("youtube", "v3", developerKey=api_key)
    comments = []
    next_page_token = None
    try:
        while True:
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=100,
                pageToken=next_page_token
            )
            response = request.execute()
            for item in response["items"]:
                comment = item["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
                comments.append(comment)
            next_page_token = response.get("nextPageToken")
            if not next_page_token:
                break
    except HttpError as e:
        error_reason = e.error_details[0].get("reason", "")
        if error_reason == "commentsDisabled":
            print(f"Comments are disabled for video: {video_id}. Skipping.")
        else:
            print(f"An error occurred for video {video_id}: {e}")
    return comments
