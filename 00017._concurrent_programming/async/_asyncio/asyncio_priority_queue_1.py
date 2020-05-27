"""
    1. asyncio.PriorityQueue + aiohttp 去访问httpbin。
    2. 数字越小，优先级越大。
    3. 每5秒producer向队列put进5个URL。
"""

import asyncio
import random
import aiohttp

URL_PREFIX = 'http://httpbin.org/get?a={}'
RANGE = range(0, 100)


async def fetch_async(a):
    async with aiohttp.request('GET', URL_PREFIX.format(a)) as r:
        data = await r.json()
    return data['args']['a']


async def produce(queue):
    while True:
        await asyncio.sleep(5)
        for num in random.sample(RANGE, 5):
            print('producing {}___'.format(num))
            item = (num, num)   # (priority number, data)
            await queue.put(item)

    await queue.join()


async def consume(queue):
    print('worker started')
    while True:
        item = await queue.get()
        num = item[0]
        rs = await fetch_async(num)
        print('consuming {}...'.format(rs))
        queue.task_done()


async def main():
    queue = asyncio.PriorityQueue()

    consumers = [
        asyncio.create_task(consume(queue))
        for _ in range(2)
    ]

    producer = asyncio.create_task(produce(queue))

    await asyncio.wait(consumers + [producer])

    print('ending')


asyncio.run(main())
