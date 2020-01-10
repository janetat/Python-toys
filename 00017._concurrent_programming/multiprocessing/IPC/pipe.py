"""
    1. 管道Pipe，返回两个connction。
    2. 默认是duplex，全双工。两边都可以send。
    3. 两个connection可以在同一个线程，可以在不同的线程，也可以在不同的进程。
"""

from multiprocessing import Process, Pipe
# from threading import Thread

def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn, ))
    # p = Thread(target=f, args=(child_conn,))  # Thread also works!
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    p.join()
