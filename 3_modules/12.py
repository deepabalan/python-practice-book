# Write a program mydoc.py to implement the funcitonality of pydoc.
# The program should take the module name as argument and print
# documentation for the module and each of the functions defined in
# that module.
# Hint: 1) The dir function to get all entries of a module
#       2) The inspect.isfunction function can be used to test if given
#          object is a function.
#       3) x.__doc__ gives the docstring for x.
#       4) The __import__ function can be used to import a module by
#          name.

import inspect


def mydoc(mod):
    f = __import__(mod)
    print f.__doc__
mydoc('os')
