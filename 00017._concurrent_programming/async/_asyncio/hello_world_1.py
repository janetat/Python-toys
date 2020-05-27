"""
    1. 模拟100个协程去完成任务。观察协程如何协同运行。
    2. 任务完成时间不定。
    3. async.sleep() always suspends the current task, allowing other tasks to run.
"""

import asyncio
import random


async def task(worker):
    print(f'{worker} started working!')

    wt = random.randrange(0, 30)    # assumed working time
    await asyncio.sleep(wt) # 

    print(f'{worker} finish his work')


async def main():
    tasks = []
    worker_prefix = 'worker_{id}'

    for num in range(100):
        worker = worker_prefix.format(id=num)
        tasks.append(task(worker))

    await asyncio.wait(tasks)


asyncio.run(main())
