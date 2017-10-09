# Write a program add.py that takes 2 numbers as command line arguments
# and prints its sum.


import sys


def add(a, b):
    return int(a) + int(b)

print add(sys.argv[1], sys.argv[2])
