# Implement a program dirtree.py that takes a directory as argument
# and prints all the files in that directory recursively as a tree.
# Hint: Use os.listdir and os.path.isdir functions.

import os
import sys


def dirtree(dirs):
    f = os.listdir(dirs)
    print dirs
    for i in f:
        a = os.path.join(dirs, i)
        if os.path.isdir(a):
            dirtree(a)
        else:
            print '|--' + a
dirtree(sys.argv[1])
