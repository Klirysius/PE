a = 6
b = 9


def f(n):
    def fn(n1):
        return n1 + n
    return fn


function = f(a)
print(function(b))
