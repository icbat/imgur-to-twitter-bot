import time
import imgur
from os import environ

print("Reading from environment variables")

sleep_seconds = int(environ["peon_sleep_seconds"])

album_id = environ["imgur_album_id"]
client_id = environ["imgur_client_id"]
client_secret = environ["imgur_client_secret"]

print("Ready to work.")
while True:
    print("Work, work.")
    images = imgur.get_images(album_id, client_id, client_secret)
    for image in images:
        print(image.link)
    print("Job's done.")
    time.sleep(sleep_seconds)
