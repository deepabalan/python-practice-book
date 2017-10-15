# Write a function array to create an 2-dimensional array. The
# function should take both dimensions as arguments. Value of each
# element can be initialized to None:


def array(r, c):
    return [[None for x in range(0, c)] for y in range(0, r) ]

a = array(2, 3)
print a

a[0][0] = 5
print a
