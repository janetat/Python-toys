"""
    1. 本示例是消费者/生产者模型。
    2. 5个消费者，每个消费者观察(wait)condition。当等到condition通知了(notify)，才可以继续切换换消费者协程执行。 
    3. 先通知一个消费者，然后通知两个消费者，然后通知所有其余的消费者。
    4. 去掉event_loop参数。
    5. asyncio.run() New in version 3.7.
"""

import asyncio


async def consumer(condition, n):
    async with condition:
        print('consumer {} is waiting'.format(n))
        await condition.wait()
        print('consumer {} triggered'.format(n))
    print('ending consumer {}'.format(n))


async def producer(condition):
    print('starting producing')

    # 唤醒/切换到另外的协程（消费者），使consumers开始执行。
    await asyncio.sleep(0.1)

    for i in range(1, 3):   # 先通知一个consumer，然后通知两个consumer
        async with condition:
            print('notifying {} consumers'.format(i))
            condition.notify(n=i)
        await asyncio.sleep(0.1)

    async with condition:
        print('notifying remaining consumers')
        condition.notify_all()

    print('ending producing')


async def main():
    condition = asyncio.Condition()

    # 设置任务以观察condition
    consumers = [
        consumer(condition, i)
        for i in range(5)
    ]

    # 安排任务以操纵condition
    # asyncio.ensure_future(producer(condition))  
    # create_task has been added in Python 3.7. Prior to Python 3.7, 
    # the low-level asyncio.ensure_future() function can be used instead:
    asyncio.create_task(producer(condition))
    # await asyncio.wait([producer(condition)]) # 错误的写法。在consumer在事件循环调度之前，producer已经执行完了，然后consumers一直阻塞。

    # 等consumers完成
    await asyncio.wait(consumers)
    # await asyncio.wait([producer(condition)]) # 错误的写法。consumer一直阻塞，produer无法开始。



asyncio.run(main()) # asyncio.run() New in version 3.7.