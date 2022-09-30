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

opt = int(input("0 - tweet\n1 - reply\n> "))

if opt == 0:
    tweet = input("Twitter message: ")
    image_path = input("Image path (skip if you don't want to post an image): ")
    if image_path != "":
        api.update_status_with_media(status=tweet, filename=image_path)
    else:
        api.update_status(status=tweet)

elif opt == 1:
    tweet_id = input("Tweet id = ")
    reply = input("Twitter message: ")
    api.update_status(status=reply, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)


print("Message sent.")
