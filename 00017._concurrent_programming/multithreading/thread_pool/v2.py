"""
    1. multiprocessing.dummy replicates the API of multiprocess ing but is no more than a wrapper around the threading module.
    2. 也就是说，multiprocessing.dummy是线程池
    3. dummy里面写了：from ..pool import ThreadPool。所以和v1.py一样
    4. dummy有人体模型的意思，模仿的意思。
"""
import time
from multiprocessing.dummy import Pool


def time_cost(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('COST: {}'.format(end - start))

    return wrapper


def fib(n):
    if n <= 2:
        return 1

    return fib(n - 1) + fib(n - 2)


@time_cost
def no_multiprocess():
    fib(35)
    fib(35)


@time_cost
def has_process_pool():
    pool = Pool(2)
    # multiprocessing.pool.Pool
    pool.map(fib, [35] * 2)


def main():
    no_multiprocess()
    has_process_pool()


main()
