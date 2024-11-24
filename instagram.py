from instagrapi import Client
import json
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get environment variables
IG_USERNAME = os.getenv('INSTAGRAM_USERNAME')
IG_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')
MONGO_URI = os.getenv('MONGO_URI')
MONGO_DB = os.getenv('MONGO_DB')
QUERY = os.getenv('QUERY')
MAX_POSTS = int(os.getenv('MAX_POSTS'))

# Connect to MongoDB
mongo_client = MongoClient(MONGO_URI)
db = mongo_client[MONGO_DB]
collection = db['posts']

cl = Client()
cl.login(IG_USERNAME, IG_PASSWORD)

hashtag_res = cl.hashtag_medias_top(QUERY, amount=MAX_POSTS)
results = []
counter = 0
for media in hashtag_res:
    if (media.media_type != 1): # Only images
        continue
    counter += 1
    post_text = media.caption_text
    post_image = str(media.thumbnail_url)
    post_likes = media.like_count
    post_comments = cl.media_comments(media.id)
    results.append({
        'post_text': post_text,
        'post_image': post_image,
        'post_likes': post_likes,
        'post_comments': [{'username': comment.user.username, 'text': comment.text} for comment in post_comments]
    })
    print(f'Post {counter} processed')
    

# Insert the results into MongoDB
collection.insert_many(results)