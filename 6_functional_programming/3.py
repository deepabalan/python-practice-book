# Write a function unflatten_dict to do reverse of flatten_dict.


def unflatten_dict(a, result=None):
    if result is None:
        result = {}

    for k, v in a.items():
        split_key = k.split('.')
        d = result
        for key in split_key[:-1]:
            if key not in d:
                d[key] = {}
            d = d[key]
        d[split_key[-1]] = v
    return result
print unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
