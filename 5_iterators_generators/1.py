# Write an iterator class reverse_iter, that takes a list and iterates
# it from the reverse direction.


class reverse_iter:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        while True:
            if len(self.n) > 0:
                return self.n.pop()
            else:
                raise StopIteration()

it = reverse_iter([1, 2, 3, 4])
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()
