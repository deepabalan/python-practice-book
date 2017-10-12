# Python has a built-in function sum to find sum of all elements of a
# a list. Provide an implementation for sum.
# sum([1, 2, 3]) gives 6


def list_sum(l):
    tot = 0;
    for i in l:
        tot += i
    return tot

print list_sum([1, 2, 3])
