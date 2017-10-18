# Write a program extcount.py to count number of files for each
# extension in the given directory. The program should take a directory
# name and print count and extension for each available file extension.


import os
import sys


def extcount(filename):
    d = {}
    filenames = os.listdir(filename)
    for name in filenames:
        s = name.split('.')[1]
        d[s] = d.get(s, 0) + 1
    for k, v in d.items():
        print v, k

extcount(sys.argv[1])    
