# Write a program wget.py to download a given URL. The program should
# accept a URL as argument, download it and save it with the basename
# of the URL. If the URL ends with a /, consider the basename as
# index.html.

import urllib
import os

def download(url):
    basename = os.path.basename(url)
    if basename == "":
        urllib.urlretrieve(url, "index.html")
    else:
        urllib.urlretrieve(url, basename)

download('http://docs.python.org/tutorial/')
