# Write a function my_enumerate that works like enumerate.


def my_enumerate(l):
    a = ((i, l[i]) for i in range(len(l)))
    for x, y in a:
        print x, y

my_enumerate(["a", "b", "c"])
