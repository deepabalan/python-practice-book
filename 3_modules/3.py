# Write a program to list all the files in the given directory along
# with their length and last modification time. The output should
# contain one line for each file containing filename, length and
# modification date separated by tabs.
# Hint: see help for os.stat

import os
import sys


def printall(filename):
    f = os.listdir(filename)
    for i in f:
        print i, os.stat(os.path.abspath(filename+'/'+i))[6], os.stat(os.path.abspath(filename+'/'+i))[8]

print printall(sys.argv[1])
