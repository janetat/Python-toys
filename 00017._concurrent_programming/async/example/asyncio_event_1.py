"""
    1. 设置两个协程等待同一个事件。
    2. 0.1秒后，在回调函数里设置事件。
"""


import asyncio
import functools


def set_event(event):
    print('setting event in callback')
    event.set()


async def coro1(event):
    print('coro1 waiting for event')
    await event.wait()
    print('coro1 triggered')


async def coro2(event):
    print('coro2 waiting for event')
    await event.wait()
    print('coro2 triggered')


async def main():
    event = asyncio.Event()
    print('event start state: {}'.format(event.is_set()))

    asyncio.get_event_loop().call_later(
        0.1, functools.partial(set_event, event)
    )

    await asyncio.wait([coro1(event), coro2(event)])
    print('event end state: {}'.format(event.is_set()))


asyncio.run(main())