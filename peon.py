import time
from os import environ
import random

import imgur
import twitter_api

print("Reading from environment variables")

sleep_seconds = int(environ["peon_sleep_seconds"])

album_id = environ["imgur_album_id"]
imgur_client_id = environ["imgur_client_id"]
imgur_client_secret = environ["imgur_client_secret"]

twitter_consumer_key = environ["twitter_consumer_key"]
twitter_consumer_secret = environ["twitter_consumer_secret"]
twitter_access_token_key = environ["twitter_access_token_key"]
twitter_access_token_secret = environ["twitter_access_token_secret"]

print("Ready to work.")
while True:
    print("Work, work.")
    images = imgur.get_images(album_id, imgur_client_id, imgur_client_secret)
    image = random.choice(images)
    print("I chose: " + image.link)
    twitter_api.post_image(image.link, twitter_consumer_key, twitter_consumer_secret, twitter_access_token_key, twitter_access_token_secret)
    print("Job's done.")
    time.sleep(sleep_seconds)
