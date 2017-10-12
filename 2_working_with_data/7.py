# Python has built-in functions min and max to compute minimum and
# maximum of a given list. Provide an implementation for these
# functions. What happens when you call your min and max functions
# with a list of strings?


def min_max(f, l):
    sort_l = sorted(l)
    if f == 'min':
        return sort_l[0]
    elif f == 'max':
        return sort_l[-1]

print min_max('min', [23, 6, 12])
print min_max('max', [2, 7, 90, 1, 18])
print min_max('min', ['apple', 'banana', 'zoo'])
print min_max('max', ['sunny', 'funny'])
