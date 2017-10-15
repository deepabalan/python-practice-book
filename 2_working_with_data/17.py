# Write a program reverse.py to print lines of a file in reverse order.

import sys


def reverse_line(filename):
    s = []
    f = open(filename)
    for line in f:
        t = line.strip()
        s.append(t)
    print s
    for i in s[::-1]:
        print i

reverse_line(sys.argv[1])
