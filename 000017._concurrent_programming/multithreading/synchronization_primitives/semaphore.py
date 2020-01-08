"""
    1. 信号量为临界资源计数器。当计数器为 0 时，acquire () 调用被阻塞。
    2. 设置Semaphore为3。
    3. 同一时刻，只有3个线程能获得资源（同时能访问资源的数量为 3）。
"""

import time
from random import random
from threading import Thread, Semaphore

sema = Semaphore(3)


def foo(tid):
    with sema:
        print('{} acquire resource'.format(tid))
        # assumed working time
        time.sleep(10)
    print('{} release resource'.format(tid))


threads = []

for i in range(10):
    t = Thread(target=foo, args=(i, ))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
