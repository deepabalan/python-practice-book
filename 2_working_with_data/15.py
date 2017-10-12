# Reimplement the unique function implemented in the earlier examples
# using sets.


def unique(l):
    return list(set(l))

print unique([1, 2, 1, 3, 4, 2])
