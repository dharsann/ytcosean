from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

uri = os.getenv("URI")

def connect_to_mongo(uri):
    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        client.admin.command('ping')
        print("Pinged your deployment. Successfully connected to MongoDB!")
        return client
    except Exception as e:
        print("Error connecting to MongoDB:", e)
        return None

