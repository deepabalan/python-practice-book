# Write a program center_align.py to center align all lines in the
# given file.

import sys


def center_align(filename):
    f = open(filename).readlines()
    for line in f:
        print line.center(100)

center_align(sys.argv[1])
