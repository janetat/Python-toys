"""
    1. multiprocessing.pool.ThreadPool
    2. 最好不要用。The multiprocessing.pool.ThreadPool is not documented as its implementation has never been completed. It lacks tests and documentation.
    3. https://stackoverflow.com/questions/46045956/whats-the-difference-between-threadpool-vs-pool-in-python-multiprocessing-modul
"""

from threading import currentThread
from multiprocessing.pool import ThreadPool
pool = ThreadPool(4)

def foo(n):
    print(currentThread().name, n ** 2)

pool.map(foo, range(11111)) 