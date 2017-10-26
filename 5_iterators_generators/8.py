# Write a function peep, that takes an iterator as argument and returns
# the first element and an equivalent iterator.


def peep(it):
    it1 = list(it)
    y = it1[0]
    return y, it1

it = iter(range(5))
x, it1 = peep(it)
print x, list(it1)
