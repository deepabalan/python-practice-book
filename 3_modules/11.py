# Write a python program zip.py to create a zip file. The program
# should take name of zip file as first argument and files to add as
# rest of the arguments.


import zipfile
import sys


def zip(filename, f1, f2):
    create_zip = zipfile.ZipFile(filename, "w")

    for i in sys.argv[1:]:
        create_zip.write(i)

zip(sys.argv[1], sys.argv[2], sys.argv[3])
