# Write a program csv2xls.py that reads a csv file and exports it as
# Excel file. The program should take two arguments. The name of the
# csv file to read as first argument and the name of the Excel file to
# write as the second argument.


import sys
import tablib


def csv2xls(f1, f2):
    data = tablib.Dataset()
    with open(f1, 'r') as f:
        data = f.read()
    with open(f2, 'wb') as f:
        f.write(data)
csv2xls(sys.argv[1], sys.argv[2])
