import twitter

def post_image(image_url, consumer_key, consumer_secret, access_token_key, access_token_secret):
    api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token_key, access_token_secret=access_token_secret)
    api.VerifyCredentials()
    api.PostMedia("", media=image_url)
