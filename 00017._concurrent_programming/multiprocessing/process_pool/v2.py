"""
    1. concurrent.futures对threading和multiprocessing的进行了高级别的抽象，暴露出统一的接口。
    2. 常用方法submit和map。如果任务是一样的，用map。
    3. 如果任务不一样，且任务可能会出现异常，则需要用submit。
    4. 本程序展示map。
"""

import time
from concurrent.futures import ProcessPoolExecutor
from functools import wraps
from os import getpid

NUMBERS = range(20, 40)


def time_cost(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('COST: {}'.format(end - start))

    return wrapper


def _fib(n):
    if n <= 2:
        return 1

    return _fib(n - 1) + _fib(n - 2)


def fib(n):
    result = _fib(n)
    print(f'current pid is: {getpid()}')
    return result


@time_cost
def has_process_pool():
    with ProcessPoolExecutor(max_workers=3) as executor:
        for num, result in zip(NUMBERS, executor.map(fib, NUMBERS)):
            print(f'fib({num} = {result})')
        print(executor._processes)


def main():
    has_process_pool()


main()
