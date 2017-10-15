# Python provides a built-in function map that applies a function to
# each element of a list. Provide an implementation for map using list
# comprehensions.


def square(x): return x * x

def map_code(f, v):
    return [f(x) for x in range(v)]

print map_code(square, 5)
