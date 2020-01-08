"""
    1. 一个线程(wait)等待特定条件，而另一个线程发出特定条件满足(notify)的信号。
    2. 实现生产者，消费者模型。
    3. Condition底层默认用RLock。
"""

import time
import threading


def consumer(cond):
    t = threading.currentThread()

    with cond:
        cond.wait()
        print('{}: get notified. Get new product.'.format(t.name))


def producer(cond):
    t = threading.currentThread()

    with cond:
        print('{}: product is made and notify all consumers'.format(t.name))
        cond.notifyAll()    # 释放waiter锁。


condition = threading.Condition()

c1 = threading.Thread(name='c1', target=consumer, args=(condition, ))
c2 = threading.Thread(name='c2', target=consumer, args=(condition, ))
p1 = threading.Thread(name='p1', target=producer, args=(condition, ))

c1.start()
time.sleep(1)
c2.start()
time.sleep(1)
p1.start()
