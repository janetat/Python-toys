"""
    1. 封装了Condition
    2. This is one of the simplest mechanisms for communication between threads: one thread signals an event and other threads wait for it.
    3. 实现生产者/消费者模型
"""
import time
import threading
from random import randint


TIMEOUT = 4


def consumer(event, l):
    t = threading.currentThread()
    while True:
        event_is_set = event.wait(TIMEOUT)  # TIMEOUT过后返回False
        print('------event_is_set', event_is_set)
        if event_is_set:
            try:
                integer = l.pop()
                print('{} popped from list by {}'.format(integer, t.name))
                event.clear()
            except IndexError:  # 为了让刚启动时不报错
                pass


def producer(event, l):
    t = threading.currentThread()
    while True:
        integer = randint(10, 100)
        l.append(integer)
        print('{} appended to list by {}'.format(integer, t.name))
        event.set()  # 设置事件
        time.sleep(5)


def main():
    event = threading.Event()
    l = []

    threads = []

    for name in ('consumer1', 'consumer2'):
        t = threading.Thread(name=name, target=consumer, args=(event, l))
        t.start()
        threads.append(t)

    p = threading.Thread(name='producer1', target=producer, args=(event, l))
    p.start()
    threads.append(p)

    for t in threads:
        t.join()


main()
