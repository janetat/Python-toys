# fib based on generator

import time


def time_profile(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('COST: {}'.format(end - start))

    return wrapper


def fib():
    a, b = 0, 1

    while True:
        a, b = b, a + b
        yield a


@time_profile
def fib_list(n):
    gen = fib()

    for _ in range(n):
        print(next(gen))


fib_list(35)
