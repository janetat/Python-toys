from threading import currentThread
from multiprocessing.pool import ThreadPool
pool = ThreadPool(4)

def foo(n):
    print(currentThread().name, n ** 2)

pool.map(foo, range(11111)) 