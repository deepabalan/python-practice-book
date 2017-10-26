# Write a function to compute the total number of lines of code,
# ignoring empty and comment lines, in all python files in the
# specified directory recursively.


import os
import sys

def pycode(dirs):
    a = ((len(open(files).readlines()), files) for files in os.listdir(dirs) if '.py' in files)
    for i in a:
        print i[0], i[1]

pycode(sys.argv[1])
