# Python provides a built-in function filter(f, a) that returns items
# of the list a for which f(item) returns true. Provide an
# implementation for filter using list comprehensions.


def even(x): return x % 2 == 0


def filter_code(f, v):
    filter_item = []
    
    for i in v:
        if f(i):
            filter_item.append(i)
    return filter_item

print filter_code(even, range(10))
print filter(even, range(10))
