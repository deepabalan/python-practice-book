# Write a function enumerate that takes a list and returns a list of
# tuples containing (index, item) for each item in the list.


def enumerate_list(l):
    return [(i, l[i]) for i in range(len(l))]

print enumerate_list(["a", "b", "c"])
