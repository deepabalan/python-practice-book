# What will be the output of the following program.
# Ans: A B
#      A B

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()

print a.f(), b.f()
print a.g(), b.g()
