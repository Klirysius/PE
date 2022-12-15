N = 10


def f2(n):
    return n**2


def f1(f):
    return f(N) - N


print(f1(f2))
