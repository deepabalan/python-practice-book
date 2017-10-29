# Write a function tree_reverse to reverse elements of a nested-list
# recursively.


def tree_reverse(l):
    reverse = []
    for x in l[::-1]:
        if isinstance(x, list):
            reverse.append(tree_reverse(x))
        else:
            reverse.append(x)
    return reverse

print tree_reverse([[1, 2], [3, [4, 5]], 6])
