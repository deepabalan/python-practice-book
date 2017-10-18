# Write a program myip.py to print the external IP address of the
# machine. Use the response from http://httpbin.org/get and read the IP
# address from there. The program should print only IP address and
# nothing else.

import urllib
import json


def myip(url):
    f = urllib.urlopen(url)
    data = json.loads(f.read())
    print data["origin"]

myip('http://httpbin.org/get')
