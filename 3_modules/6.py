# Write a program antihtml.py that takes a URL as argument, downloads
# the html from web and print it after stripping html tags.

import urllib
import os
import sys
import re


def antihtml(url):
    basename = os.path.basename(url)
    if basename == "":
        filename = 'index.html'
    else:
        filename = basename
    urllib.urlretrieve(url, filename)
    f = open(filename)
    match = re.findall(r'(>)([\w+\s]*)(<)', f.read())
    for line in match:
        print line[1]

antihtml(sys.argv[1])
