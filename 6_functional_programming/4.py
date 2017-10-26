# Write a function treemap to map a function over nested list.


def treemap(f, l):
    res = []
    for x in l:
        if isinstance(x, list):
            res.append(treemap(f, x))
        else:
            res.append(f(x))
    return res

print treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
