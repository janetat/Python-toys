"""
    1. asyncio有自己的队列。Queue(FIFO), PriortyQueue.
    2. queue.Queue是给线程用的，multiprocessing.Queue是给进程用的.
"""

import asyncio


async def consumer(num, q):
    print('consumer {}: starting'.format(num))

    while True:
        print('consumer {}: waiting for item'.format(num))
        item = await q.get()
        print('consumer {}: has item {}'.format(num, item))

        if item is None:
            # None is the signal to stop.
            q.task_done()
            break
        else:
            wt = 0.1 * item  # assumed working time
            print('consuer {}: consumed item {} for {}s'.format(num, item, wt))
            await asyncio.sleep(wt) # 切换到其他协程。
            q.task_done()

    print('consumer {}: ending'.format(num))


async def producer(q, num_workers):
    print('producer: starting')

    for i in range(num_workers * 3):
        await q.put(i)
        print('producer: added task {} to the queue'.format(i))

    print('producer: adding stop signals to the queue')
    for i in range(num_workers):
        await q.put(None)

    print('producer: waiting for queue to empty')
    await q.join()
    print('producer: ending')


async def main(num_consumers):
    q = asyncio.Queue(maxsize=num_consumers)

    # Schedule the consumer tasks.
    consumers = [
        asyncio.create_task(consumer(num, q))
        for num in range(num_consumers)
    ]

    # Schedule the producer task.
    prod = asyncio.create_task(producer(q, num_consumers))

    # Wait for all of the coroutines to finish.
    await asyncio.wait(consumers + [prod])


asyncio.run(main(2))
