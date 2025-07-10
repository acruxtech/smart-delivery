def cache(func):
    res = {}

    def inner(*args):
        if args not in res:
            res[args] = func(*args)
        return res[args]

    return inner


@cache
def multiply(a, b):
    return a * b


print(multiply(2, 3))
