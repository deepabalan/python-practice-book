# Write a function permute to compute all possible permutations of
# elements of a given list.

import itertools


def permute(l):
    return [list(x) for x in itertools.permutations(l)]

print permute([1, 2, 3])
