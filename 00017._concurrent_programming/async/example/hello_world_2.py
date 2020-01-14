"""
    1. 研究如何写才能真正实现协程并发。（如何正确使用asyncio）
    2. Based on python 3.7.4. 
"""

import asyncio
import time


def show_perf(func):
    print('*' * 20)
    start = time.perf_counter()
    asyncio.run(func())
    end = time.perf_counter()
    print(f'{func.__name__} Cost: {end - start}')


async def a():
    print('Suspending a')
    await asyncio.sleep(3)
    print('Resuming a')


async def b():
    print('Suspending b')
    await asyncio.sleep(1)
    print('Resuming b')


async def main_1():
    # 这样写不能并发，变成串行了。4秒
    await a()
    await b()


async def main_2():
    # 这样写可以。3秒。
    task_1 = asyncio.create_task(a())
    task_2 = asyncio.create_task(b())
    await task_1
    await task_2


async def main_3():
    # 这样写可以。3秒
    await asyncio.gather(a(), b())


async def main_4():
    # 这样写可以。3秒
    task_1 = asyncio.create_task(a())
    await b()
    await task_1


async def main_5():
    # 这样写不行。4秒
    task_1 = asyncio.create_task(a())
    await task_1
    await b()


async def main_6():
    # 这样写不行。4秒
    await asyncio.create_task(a())
    await asyncio.create_task(b())

# show_perf(main_1)
# show_perf(main_2)
# show_perf(main_3)
# show_perf(main_4)
# show_perf(main_5)
show_perf(main_6)
