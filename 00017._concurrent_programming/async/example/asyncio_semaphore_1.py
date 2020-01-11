"""
    1. 抓取http://httpbin.org/get?a=X这样的页面，X为1-10000的数字。
    2. 用Semaphore控制同一时刻的并发量。
"""

import aiohttp
import asyncio
from pprint import pprint

NUMBERS = range(11)
URL = 'http://httpbin.org/get?a={}'
SEMAPHORE = 3


async def fetch_async(num):
    async with aiohttp.request('GET', URL.format(num)) as r:
        data = await r.json()
    return data


async def print_result(num):
    sema = asyncio.Semaphore(SEMAPHORE)
    async with sema:
        result = await fetch_async(num)
        # pprint(r)
        pprint('fetch({} = {})'.format(num, result))


async def main():
    await asyncio.gather(
        *[print_result(num) for num in NUMBERS]
    )

asyncio.run(main())
