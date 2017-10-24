# Write a function findfiles that recursively descends the directory
# tree for the specified directory and generates paths of all the files
# in the tree.

import os
import sys


def findfiles(dirname):
    for dirpath, dirnames, filenames in os.walk(dirname):
        print dirpath, dirnames, filenames

findfiles(sys.argv[1])
