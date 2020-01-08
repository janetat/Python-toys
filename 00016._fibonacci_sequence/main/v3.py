# recursion fib with lru_cache

import time
from functools import lru_cache


def time_profile(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('COST: {}'.format(end - start))

    return wrapper


@lru_cache(maxsize=2)
def fib(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


@time_profile
def fib_list(n):
    for _ in range(n):
        print(fib(_))


fib_list(35)
