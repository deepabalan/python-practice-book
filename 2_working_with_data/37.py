# Write a function valuesort to sort values of a dictionary based on
# the key.


def valuesort(d):
    return [d[i] for i in sorted(d) ]

print valuesort({'x': 1, 'y': 2, 'a': 3})
