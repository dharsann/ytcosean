from http.client import responses
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

api_key = os.getenv("API_KEY")

def get_channel_videos(channel_id, api_key):
    youtube = build("youtube", "v3", developerKey=api_key)
    request = youtube.channels().list(
        part='contentDetails',
        id=channel_id
    )
    response = request.execute()
    uploads_playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    video_ids = []
    next_page_token = None
    while True:
        playlist_request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=uploads_playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        playlist_response = playlist_request.execute()
        for item in playlist_response['items']:
            video_ids.append(item['contentDetails']['videoId'])
        next_page_token = playlist_response.get('nextPageToken')
        if not next_page_token:
            break
    return video_ids
