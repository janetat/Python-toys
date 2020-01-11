"""
    1. 主线程首先acquire加锁，然后2秒后释放锁。
    2. 然后用这个锁去同步100个worker协程。
"""

import asyncio
import functools

def _unlock(lock):
    print('callback releasing lock')
    lock.release()
    print('-----------------')


async def _async_task(worker, lock):
    print('{} waiting for the lock'.format(worker))
    async with lock:
        print('{} acquired lock'.format(worker))
        await asyncio.sleep(1)
    print('{} released lock'.format(worker))
    print('-----------------')


async def main(loop):
    tasks = []
    lock = asyncio.Lock()
    worker_prefix = 'worker_{id}'
    unlock = functools.partial(_unlock, lock)
    async_task = functools.partial(_async_task, lock=lock)

    # 一开始获取锁。两秒后才放出。就像跑步比赛前的准备时间。
    await lock.acquire()
    loop.call_later(2, unlock)

    for _id in range(100):
        worker = worker_prefix.format(id=_id)
        tasks.append(async_task(worker))

    await asyncio.gather(
        *tasks
    )


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
