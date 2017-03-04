import time
from os import environ

print("Reading from environment variables")

sleep_seconds = environ["peon_sleep_seconds"]

print("Ready to work.")
while True:
    print("Work, work.")

    print("Job's done.")
    time.sleep(sleep_seconds)
