"""
    1. Lock是互斥锁mutex。其实相当于信号量为1。
    2. 本程序为加锁的条件下，100个线程去操作一个全局变量。操作为+1。
    3. 加锁的情况下，结果和预期相符，为100。
"""

import time
from threading import Thread, Lock

value = 0
lock = Lock()


def global_value_plus_1():
    global value
    with lock:
        new_value = value + 1
        time.sleep(0.001)
        # time.sleep(0.1)
        value = new_value


threads = []

for i in range(100):
    t = Thread(target=global_value_plus_1)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(value)
