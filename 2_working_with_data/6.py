# Write a function reverse to reverse a list. Can you do this without
# using list slicing?
# reverse([1, 2, 3, 4]) gives [4, 3, 2, 1]
# reverse(reverse([1, 2, 3, 4])) gives [1, 2, 3, 4]


def reverse_list(l):
    rev = []
    i = len(l) - 1
    while i >= 0:
        rev.append(l[i])
        i -= 1
    return rev

print reverse_list([1, 2, 3, 4])
print reverse_list(reverse_list([1, 2, 3, 4]))
