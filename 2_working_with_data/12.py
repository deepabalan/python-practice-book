# Write a function group(list, size) that take a list and splits into
# smaller lists of given size.


def group(l, s):
    t = []
    i = 0
    j = s

    while i < len(l):
        t.append(l[i:j])
        i = j
        j += s
    return t

print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
