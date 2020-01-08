"""
    1. 队列在并发开发中最常用的。
    2. 实现生产者/消费者模型。生产者把生产的消息放入队列，消费者从这个队列中对去对应的消息执行。
    3. 重点方法：put, get, task_done, join
    4. queue模块还有PriorityQueue, LifoQueue
"""

import time
import threading
from random import random
from queue import Queue

q = Queue()


def double(n):
    return n * 2


def producer():
    while True:
        # assumed working time
        wt = random()
        time.sleep(wt)
        q.put((double, wt))


def consumer():
    while True:
        task, arg = q.get()
        print('current thread is {current_thread}, arg is {arg}, task result is {task_result}'.format(
            current_thread=threading.currentThread().name, arg=arg, task_result=task(arg)))
        q.task_done()


def main():
    threads = []
    c1 = threading.Thread(name='c1', target=consumer)
    c2 = threading.Thread(name='c2', target=consumer)
    p1 = threading.Thread(name='p1', target=producer)

    threads.extend([c1, c2, p1])

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


main()
