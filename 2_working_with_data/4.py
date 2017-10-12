# Implement a function product, to compute product of a list of
# numbers.
# product([1, 2, 3]) gives 6


def product(l):
    res = 1
    for i in l:
        res *= i
    return res

print product([1, 2, 3])
