# Write a function invertdict to interchange keys and values in a
# dictionary. For simplicity, assume that all values are unique.

def invertdict(d):
    res = {}
    for i, v in d.items():
        res[v] = i
    return res

print invertdict({'x': 1, 'y': 2, 'z': 3})
