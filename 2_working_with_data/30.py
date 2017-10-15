# Write a python function parse_csv to parse 
# csv(comma separated values) files.


import sys


def parse_csv(filename):
    return [line.strip().split(',') for line in open(filename)]

print parse_csv(sys.argv[1])
