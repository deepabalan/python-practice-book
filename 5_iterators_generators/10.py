# Implement a function izip that works like itertools.izip.


def izip(l1, l2):
    a = ((l1[i], l2[i]) for i in range(len(l1)) if len(l1) == len(l2))
    for x, y in a:
        print x, y
izip(["a", "b", "c"], [1, 2, 3])
