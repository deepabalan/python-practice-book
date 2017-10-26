# Write a function to compute the total number of lines of code in all
# python files in the specified directory recursively.


import os
import sys


def find_py_line(directory):
    listdirs = os.listdir(directory)
    for files in listdirs:
        if '.py' in files:
            #print os.path.abspath(files)
            f = len(open(files).readlines())
            print files, f

find_py_line(sys.argv[1])
