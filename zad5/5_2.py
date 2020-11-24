import functools


def pamiec(func):
    buffer = {}

    @functools.wraps(func)
    def wrapper(*args):
         if args in buffer:
             return buffer[args]
         else:
             temp = func(*args)
             buffer[args] = temp
             return temp
    return wrapper


@pamiec
def fibonacci(n):
    return n if 0 <= n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


for i in range(100):
    print(fibonacci(i))

