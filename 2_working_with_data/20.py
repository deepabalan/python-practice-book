# Implement unix command grep. The grep command takes a string and a
# file as arguments and prints all lines in the file which contain the
# specified string.

import sys


def unix_grep(filename, word):
    f = open(filename).readlines()
    for ch in f:
        if word in ch:
            print ch.strip('\n')

unix_grep(sys.argv[1], sys.argv[2])    
