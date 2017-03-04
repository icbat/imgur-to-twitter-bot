from imgurpython import ImgurClient
def get_images(album_id, client_id, client_secret):
    client = ImgurClient(client_id, client_secret)
    return client.get_album_images(album_id)
