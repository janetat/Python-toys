"""
    1. 线程池
    2. from multiprocessing.pool import Pool
    3. 强调：任务的执行周期决定于 CPU 核数、任务分配算法、操作系统的时间片分配算法（调度算法）
"""

import time
from multiprocessing.pool import Pool


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
