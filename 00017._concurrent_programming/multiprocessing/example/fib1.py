"""
    多线程、多进程、单线程各计算两次fib。
"""

import time
import multiprocessing
import threading


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
def has_multiprocess():
    processes = []

    for i in range(2):
        p = multiprocessing.Process(target=fib, args=(35, ))
        p.start()
        processes.append(p)

    for process in processes:
        process.join()


@time_cost
def has_multithreading():
    threads = []

    for i in range(2):
        t = threading.Thread(target=fib, args=(35, ))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()


def main():
    no_multiprocess()
    has_multiprocess()
    has_multithreading()

main()