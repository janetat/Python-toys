"""
    1. 多进程的队列，from multiprocessing import Queue
    2. 多线程的队列，from queue import Queue
    3. 本程序是生产者/消费者模型，用 2 个队列：一个队列用于存储待完成的任务（JoinableQueue，有join，task_done），另外一个用于存储任务完成后的结果（Queue）
"""
import time
from multiprocessing import Process, JoinableQueue, Queue
from random import random


tasks_queue = JoinableQueue()
results_queue = Queue()


def task_double(n):
    return n * 2


def producer(in_queue):
    while True:
        wt = random()   # assumed working time
        time.sleep(wt)
        in_queue.put((task_double, wt))

        if wt > 0.9:    # 10% chance to stop producing
            in_queue.put(None)
            print('stop producer')
            break


def consumer(in_queue, out_queue):
    while True:
        task = in_queue.get()
        if task is None:
            break

        func, arg = task
        result = func(arg)
        in_queue.task_done()
        out_queue.put((f'Original arg: {arg}', f'After double: {result}'))


def main():
    processes = []

    p = Process(target=producer, args=(tasks_queue,))
    p.start()
    processes.append(p)

    p = Process(target=consumer, args=(tasks_queue, results_queue))
    p.start()
    processes.append(p)

    tasks_queue.join()

    for p in processes:
        p.join()

    while True:
        if results_queue.empty():
            break

        result = results_queue.get()
        print('Result:', result)


main()
