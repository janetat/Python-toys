import asyncio


async def a():
    await asyncio.sleep(1)
    return 'A'


def callback(future):
    print(f'call back is back! Result: {future.result()}')


async def main():
    task_1 = asyncio.create_task(a())
    task_1.add_done_callback(callback)
    await task_1

asyncio.run(main())


loop = asyncio.get_event_loop()

loop.run_in_executor()