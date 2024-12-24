from googleapiclient.discovery import build
from get_allvideos import get_channel_videos
import json

def get_video_statistics(video_id, api_key):
    try:
        youtube = build("youtube", "v3", developerKey=api_key)
        request = youtube.videos().list(
            part="statistics",
            id=video_id
        )
        response = request.execute()
        if "items" in response and len(response["items"]) > 0:
            stats = response["items"][0]["statistics"]
            return {
                "video_id": video_id,
                "viewCount": int(stats.get("viewCount", 0)),
                "likeCount": int(stats.get("likeCount", 0)),
                "dislikeCount": int(stats.get("dislikeCount", 0))
            }
        else:
            return {"video_id": video_id, "error": "No data found"}
    except Exception as e:
        return {"video_id": video_id, "error": str(e)}
