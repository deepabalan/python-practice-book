# Write a function flatten_dict to flatten a nested dictionary by
# joining the keys with . character.


def flatten_dict(a, result=None):
    if result is None:
        result = {}

    for k, v in a.items():
        if isinstance(v, dict):
            for key, val in v.items():
                result[k+'.'+key] = val
                flatten_dict(result)
        else:
            result[k] = v
    return result

print flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
