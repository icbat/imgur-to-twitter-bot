# saves local files given what's pasted into urls
urls = []

import urllib.request

for index, url in enumerate(urls):
    urllib.request.urlretrieve(url, str(index) + ".jpg")
