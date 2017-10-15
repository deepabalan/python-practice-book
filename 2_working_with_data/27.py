# Write a function triplets that takes a number n as argument and
# returns a list of triplets such that sum of first two elements of the
# triplet equals the third element using numbers below n. Please note
# that (a, b, c) and (b, a, c) represent same triplet.


def triplets(n):
    return [(a, b, c) for a in range(1, n) for b in range(a, n) for c in range(1, n) if a + b == c ]

print triplets(5)
