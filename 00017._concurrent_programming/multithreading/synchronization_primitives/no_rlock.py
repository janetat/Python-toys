"""
    1. acquire () 能够不被阻塞的被同一个线程调用多次。
    2. release () 需要调用与 acquire () 相同的次数才能释放锁。(An RLock on the other hand, can be acquired multiple times, by the same thread)
    3. 什么时候用RLock? https://stackoverflow.com/a/16568426/5955399
"""

import threading

lock = threading.Lock()

lock.acquire()

ret = lock.acquire()    # 不注释本行时，一直阻塞。因为Lock互斥锁相当于Semaphore为1，这里进行了两次acquire操作，所以阻塞。
print('main thread end')
