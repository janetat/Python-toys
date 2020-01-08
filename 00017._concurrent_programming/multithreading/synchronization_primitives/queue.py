"""
    1. 优先级队列是线程安全的。
    2. 底层是heapq。
    3. 数字越小，优先级越大。任务越先被处理。
"""

import time
import threading
from random import randint
from queue import PriorityQueue


q = PriorityQueue()


def double(n):
    return n * 2


def producer():
    count = 0
    while True:
        if count > 5:
            break
        pri = randint(0, 100)
        print('put:{}'.format(pri))
        q.put((pri, double, pri))  # (priority, func, args)
        count += 1


def consumer():
    while True:
        if q.empty():
            break
        pri, task, arg = q.get()
        print('[PRI:{}] {} * 2 = {}'.format(pri, arg, task(arg)))
        q.task_done()


def main():
    t = threading.Thread(target=producer)
    t.start()
    time.sleep(1)
    t = threading.Thread(target=consumer)
    t.start()


main()
