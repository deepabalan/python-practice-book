# The above wrap program is not so nice because it is breaking the line
# at middle of any word. Can you write a new program wordwrap.py that
# works like wrap.py, but breaks the line only at the word boundaries?


import sys
import textwrap

def word_wrap(filename, width):
    f = open(filename).readlines()
    for line in f:
        res = textwrap.wrap(line, width)
        print res[0] + '\n' + res[1]

word_wrap(sys.argv[1], int(sys.argv[2]))
