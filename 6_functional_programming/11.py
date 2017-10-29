# Write a function vectorize which takes a function f and return a
# new function, which takes a list as argument and calls f for every
# element and returns the result as a list.


def square(x): return x * x


def vectorize(f):
    def g(x):
        res = []
        for i in x:
            a = f(i)
            res.append(a)
        return res
    return g

y = vectorize(square)
print y([1, 2, 3])
s = vectorize(len)
print s(["hello", "world"])
