"""
    1. Lock是互斥锁mutex。其实相当于信号量为1。
    2. 本程序为不加锁的条件下，100个线程去操作一个全局变量。操作为+1。
    3. 没有锁的情况下，结果和预期不符，不是100。
"""

import time
from threading import Thread

value = 0


def global_value_plus_1():
    global value
    new_value = value + 1
    time.sleep(0.01)  # 让线程可以切换
    # time.sleep(0.1) # 如果sleep时间比较长的话，全局变量value是1。
    value = new_value


threads = []

for i in range(100):
    t = Thread(target=global_value_plus_1)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(value)
