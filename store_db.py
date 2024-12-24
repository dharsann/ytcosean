from analyze_sentiment import analyze_video_sentiment
from connect_db import connect_to_mongo
from get_allvideos import get_channel_videos
from get_titleduration import get_video_title_and_duration
from get_comments import get_video_comments
from get_statistics import get_video_statistics
from dotenv import load_dotenv
import os

# uri = os.getenv("URI")
# api_key = os.getenv("API_KEY")

def store_sentiments_db(uri, api_key):
    mongo_client = connect_to_mongo(uri)
    if not mongo_client:
        print("Failed to connect to MongoDB. Exiting.")
        return
    db = mongo_client["YoutubeData"]
    collection = db["comments"]
    video_ids = get_channel_videos(channel_id, api_key)
    for video_id in video_ids:
        print(f"Processing video: {video_id}")
        comments_data = get_video_comments(video_id, api_key)
        score = analyze_video_sentiment(comments_data)
        document = {
            "video_id": video_id,
            "sentiment": score
        }
        collection.insert_one(document)
        print(f"Data for video {video_id} inserted successfully.")
    print("All data has been processed and stored in MongoDB.")

def store_statistics_db(uri, api_key):
    mongo_client = connect_to_mongo(uri)
    if not mongo_client:
        print("Failed to connect to MongoDB. Exiting.")
    db = mongo_client["YoutubeData"]
    collection = db["statistics"]
    video_ids = get_channel_videos(channel_id, api_key)
    for video_id in video_ids:
        print(f"Processing video: {video_id}")
        stats = get_video_statistics(video_id, api_key)
        document = {
            "video_id": video_id,
            "viewCount": stats.get("viewCount", 0),
            "likeCount": stats.get("likeCount", 0),
            "dislikeCount": stats.get("dislikeCount", 0),
        }
        collection.insert_one(document)
    print("All data has been processed and stored in MongoDB.")

def store_details_db(uri, api_key):
    mongo_client = connect_to_mongo(uri)
    if not mongo_client:
        print("Failed to connect to MongoDB. Exiting.")
    db = mongo_client["YoutubeData"]
    collection = db["details"]
    video_ids = get_channel_videos(channel_id, api_key)
    for video_id in video_ids:
        print(f"Processing video: {video_id}")
        details = get_video_title_and_duration(video_id, api_key)
        document = {
            "video_id": video_id,
            "title": details.get("title", 0),
            "duration": details.get("duration", 0)
        }
        collection.insert_one(document)
    print("All data has been processed and stored in MongoDB.")

if __name__ == '__main__':
    channel_id = "UCkQWNxPGUliGeWSLf-3aXkw"
    uri = "mongodb+srv://dharsannofficial:saidharsann2011@cluster0.wsvow.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    api_key = "AIzaSyCX1FMks_AgLlLutKzKfoUM8xUutxur2Z4"
    store_details_db(uri, api_key)