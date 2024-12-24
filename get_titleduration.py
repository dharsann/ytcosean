from googleapiclient.discovery import build
import json
import html
import re
import isodate

def get_video_title_and_duration(video_id, api_key):
    youtube = build("youtube", "v3", developerKey=api_key)
    try:
        request = youtube.videos().list(
            part="snippet,contentDetails",
            id=video_id
        )
        response = request.execute()
        if "items" in response and len(response["items"]) > 0:
            item = response["items"][0]
            raw_title = item["snippet"]["title"]
            iso_duration = item["contentDetails"]["duration"]
            cleaned_title = re.sub(r"[^\x00-\x7F]+|#[^\s]+", "", raw_title).strip()
            duration_timedelta = isodate.parse_duration(iso_duration)
            formatted_duration = f"{duration_timedelta.seconds // 60}:{duration_timedelta.seconds % 60:02}"
            return {
                "video_id": video_id,
                "title": cleaned_title,
                "duration": formatted_duration
            }
        else:
            return {"video_id": video_id, "error": "No data found"}
    except Exception as e:
        return {"video_id": video_id, "error": str(e)}

if __name__ == "__main__":
    api_key = "AIzaSyCX1FMks_AgLlLutKzKfoUM8xUutxur2Z4"
    video_id = "Rc85uLdAV20"
    video_details = get_video_title_and_duration(video_id, api_key)
    print(json.dumps(video_details, indent=4))
