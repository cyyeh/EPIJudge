# mutable arguments should have None as their default values
def foo(x=[]):
    x.append(1)
    return x

res = foo()
print(res)
res = foo()
print(res)


def foo(x, y, z):
    return x * x + y * y + z * z

foo(1, 2, 3)
foo(1, y=2, z=3)
foo(1, z=3, y=3)
# syntax error: keyword arguments must follow positional arguments
foo(x=1, 2, z=3)
# syntax error: a variable cannot be assigned twice
foo(1, x=2, z=3, y=4)


