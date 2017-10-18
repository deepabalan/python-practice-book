# Write a program links.py that takes URL of a webpage as argument and
# prints all the URLs linked from that webpage.


import urllib
import re
import sys


def links(url):
    f = urllib.urlopen(url)
    lines = re.findall(r'http://\w+\S*', f.read())
    for line in lines:
        print line
links(sys.argv[1])
