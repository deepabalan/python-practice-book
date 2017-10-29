# Write a function count_change to count the number of ways to change
# any given amount. Available coins are also passed as arguments to
# the function.


def count_change(amount, xlist):
    if amount == 0:
        return 1
    elif amount < 0:
        return 0
    elif len(xlist) == 0:
        return 0
    else:
        return count_change(amount-xlist[0], xlist) + count_change(amount, xlist[1:])

print count_change(10, [1, 5])
print count_change(10, [1, 2])
print count_change(100, [1, 5, 10, 25, 50])
