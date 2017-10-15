# Implement unix commands head and tail. The head and tail commands
# take a file as argument and prints its first and last 10 lines of the
# file respectively.

import sys


def unix_head(fun, filename):
    res = []
    f = open(filename)
    for line in f:
        res.append(line.strip())
    if fun == 'head':
        for x in res[:10]:
            print x
    elif fun == 'tail':
        for x in res[-10:]:
            print x

unix_head(sys.argv[1], sys.argv[2])

