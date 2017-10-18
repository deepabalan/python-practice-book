# Generalize the above implementation of csv parser to support any
# delimiter and comments.

import sys


def parse_txt(filename, d1, d2):
    return [line.strip().split(d1) for line in open(filename).readlines() if line[0] != d2]

print parse_txt(sys.argv[1], '!', '#')
