# Write a program wrap.py that takes filename and width as arguments
# and wraps lines longer than width.


import sys


def wrap(filename, width):
    f = open(filename).readlines()
    for line in f:
        if len(line) > width:
            print line[:width] + '\n' + line[width:]
        else:
            print line

wrap(sys.argv[1], int(sys.argv[2]))
