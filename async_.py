#!/usr/bin/python
#coding: utf-8
#@Author:liyichao
# import time
# import asyncio
#
# now = lambda: time.time()
#
# async def do_some_work(x):
#     print('Waiting: ', x)
# start = now()
# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine)
# print('TIME: ', now() - start)

#--------------

# import asyncio
# import time
#
# now = lambda: time.time()
#
# async def do_some_work(x):
#     print('Waiting: ', x)
# start = now()
# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
# #task = loop.create_task(coroutine)
# print(task)
# loop.run_until_complete(task)
# print(task)
# print('TIME: ', now() - start)

#执行回调函数
# import time
# import asyncio
# import functools
# now = lambda: time.time()
# async def do_some_work(x):
#     print('Waiting: ', x)
#     return 'Done after {}s'.format(x)
# # # def callback(future):
# # #     print('Callback: ', future.result())
# # def callback(t, future):
# #     print('Callback:', t, future.result())
# #
# start = now()
# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# # task = asyncio.ensure_future(coroutine)
# # task.add_done_callback(functools.partial(callback, 2))  #偏函数的语法
# # # task.add_done_callback(callback)
#
# task = asyncio.ensure_future(coroutine)  #直接使用future代替回调函数打印语法
# loop.run_until_complete(task)
#
# print('Task ret: {}'.format(task.result()))
# print('TIME: {}'.format(now() - start))
# # loop.run_until_complete(task)
# # print('TIME: ', now() - start)

#开始阻塞
# import asyncio
# import time
# now = lambda: time.time()
# async def do_some_work(x):
#     print('Waiting: ', x)
#     await asyncio.sleep(x)
#     return 'Done after {}s'.format(x)
# start = now()
# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
# loop.run_until_complete(task)
#
# print('Task ret: ', task.result())
# print('TIME: ', now() - start)

#开始并发，创建协程列表
# import asyncio
# import time
# now = lambda: time.time()
# async def do_some_work(x):
#     print('Waiting: ', x)
#     await asyncio.sleep(x)
#     return 'Done after {}s'.format(x)
# start = now()
# coroutine1 = do_some_work(1)
# coroutine2 = do_some_work(2)
# coroutine3 = do_some_work(4)
# tasks = [
#     asyncio.ensure_future(coroutine1),
#     asyncio.ensure_future(coroutine2),
#     asyncio.ensure_future(coroutine3)
# ]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))   #调用任务队列执行的方式
# for task in tasks:
#     print('Task ret: ', task.result())
# print('TIME: ', now() - start)

#嵌套协程
# import asyncio
# import time
# now = lambda: time.time()
# async def do_some_work(x):
#     print('Waiting: ', x)
#     await asyncio.sleep(x)
#     return 'Done after {}s'.format(x)
# async def main():
#     coroutine1 = do_some_work(1)
#     coroutine2 = do_some_work(2)
#     coroutine3 = do_some_work(4)
#     tasks = [
#         asyncio.ensure_future(coroutine1),
#         asyncio.ensure_future(coroutine2),
#         asyncio.ensure_future(coroutine3)
#     ]
#     dones, pendings = await asyncio.wait(tasks) #挂起后，可以统一阻塞完成后继续执行
#     for task in dones:
#         print('Task ret: ', task.result())
# start = now()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# print('TIME: ', now() - start)

#协程停止
import asyncio
import time
now = lambda: time.time()
async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)
# coroutine1 = do_some_work(1)
# coroutine2 = do_some_work(2)
# coroutine3 = do_some_work(2)
# tasks = [
#     asyncio.ensure_future(coroutine1),
#     asyncio.ensure_future(coroutine2),
#     asyncio.ensure_future(coroutine3)
# ]

async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(2)
    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]
    done, pending = await asyncio.wait(tasks)
    for task in done:
        print('Task ret: ', task.result())

start = now()
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(main())
try:
    # loop.run_until_complete(asyncio.wait(tasks))
    loop.run_until_complete(task)
except KeyboardInterrupt as e:
    print(asyncio.Task.all_tasks())
    # for task in asyncio.Task.all_tasks():
    #     print(task.cancel())
    print(asyncio.gather(*asyncio.Task.all_tasks()).cancel())  #使用这种方式调用，不需要登陆在循环里面停止
    loop.stop()
    loop.run_forever()
finally:
    loop.close()
    # pass
print('TIME: ', now() - start)
    
