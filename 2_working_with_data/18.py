# Write a program to print each line of a file in reverse order.

import sys


def reverse_line(filename):
    s = []    
    f = open(filename)
    for line in f:
        t = line.strip().split()
        s.append(t[::-1])
    for i in s:
        print ' '.join(i)

reverse_line(sys.argv[1])
