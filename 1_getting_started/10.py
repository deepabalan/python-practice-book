# What will be the output of the following program?
# Ans: 1, error

x = 1

def f():
    y = x
    x = 2
    return x + y
print x
print f()
print x
