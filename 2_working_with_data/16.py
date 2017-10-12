# Write a function extsort to sort a list of files based on extension.


def extsort(l):
    return sorted(l, key=lambda x: x.split('.')[1])
print extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
