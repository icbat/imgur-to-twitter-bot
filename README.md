# imgur-to-twitter-bot
Posts a random picture from an imgur album

## Running the bot

1. Setup environment variables as described below
1. Optionally `virtualenv . ` and activate the new virtual environment (differs by platform)
1. `pip install -r requirements.txt`
1. Whenever you want to post, run `python src/peon.py`
1. Optionally setup a scheduled task to run the above commmand on a set interval

## Environment variables

These need to be configured in the environment before running the bot

## Imgur

To get these, you need to:
1. Create or login with your imgur account at api.imgur.com
2. Register your application (should be available at api.imgur.com)
3. When choosing Authorization Type for your imgur app, you can choose Anonymouse usage

- imgur_album_id - the album on imgur to pull from. found in the album's url
- imgur_client_id - your client ID for Imgur's API
- imgur_client_secret - your client secret for Imgur's API (not actually needed)

## Twitter

To get these, you need to:
1. create a Twitter account for your bot
2. Login to dev.twitter.com as that user
3. Create an application

Then you can find this information under the application's info

- twitter_consumer_key - your twitter consumer key
- twitter_consumer_secret - your twitter consumer secret
- twitter_access_token_key - your twitter access token key
- twitter_access_token_secret - your twitter access token secret

## Miiverse scripts/step

Also included in this repo is a short set of scripts to download pictures from Nintendo's Miiverse

1. Login to miiverse
2. Open console there
3. paste into console the code from `localscripts/saveMiiverse.js`
4. Take the resulting array from that and paste that into `localscripts/saveurls.py` as `urls`
5. Run `localscripts/saveurls.py`, which will save all the pictures locally
6. Upload these to an imgur album
7. Use `localscripts/deleteMiiverse.js` as needed to clear up space of your now-backed up miiverse
8. ??
9. Profit!
