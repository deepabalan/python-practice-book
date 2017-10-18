# Write a program to list all files in the given directory.

import os
import sys


def listdir(filename):
    for i in os.listdir(filename):
        print i

listdir(sys.argv[1])
