# Write a function to compute the number of python files in a specified
# directory recursively.


import os
import sys


def pycount(files):
    return [f for f in files if '.py' in f]

files = os.listdir(sys.argv[1])
pyfile = pycount(files)
print len(pyfile)
