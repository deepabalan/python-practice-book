# Implement a function product to multiply 2 numbers recursively using
# + and - operators only.


def product(x, y):
    if y == 0:
        return 0
    else:
        return x + product(x, y-1)

print product(9, 27)
