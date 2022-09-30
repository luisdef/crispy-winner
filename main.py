import os
from unicodedata import numeric
import tweepy
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
TOKEN = os.getenv("TOKEN")
TOKEN_SECRET = os.getenv("TOKEN_SECRET")

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(TOKEN, TOKEN_SECRET)
api = tweepy.API(auth)

tweet = input("Twitter message: ")
image_path = input("Image path (skip if you don't want to post an image): ")

if image_path != "" and numeric(image_path):
    api.update_status_with_media(status=tweet, filename=image_path)
else:
    api.update_status(status=tweet)

print("Message sent.")
