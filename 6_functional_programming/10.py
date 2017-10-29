# Write a function profile, which takes a function as arguments and
# returns a new function, which behaves exactly similar to the given
# function, except that it prints the time consumed in executing it.

import time


def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print fib(20)
def profile(f):
    def g(x):
        t = 0
        begin = time.time()
        a = f(x)
        t = time.time() - begin
        return 'time taken ' + str(t) + ' sec'
    return g

fib = profile(fib)
print fib(20)
