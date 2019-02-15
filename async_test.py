#!/usr/bin/python
#coding: utf-8
#@Author:liyichao
import asyncio
import functools
from asyncio import Queue

queue=Queue()

async def do_work(p):
    print('install mysql %d'%p)
    await asyncio.sleep(p)
    await queue.put(p)  #使用队列的好处，可以并发，如果是全局队列则会阻塞在这个地方
    return 'install mysql %d done'%p

def callback(future,t):
    print('in callback %d'%t)

async def main():
    task=[asyncio.ensure_future(do_work(4)),asyncio.ensure_future(do_work(6))]
    # task[0].add_done_callback(callback)
    task[0].add_done_callback(functools.partial(callback,t=2))
    done,pend=await asyncio.wait(task)

#<Task finished coro=<do_work() done, defined at D:/02-skills/python/500test/async_test.py:7> result='install mysql 4 done'>
#<Task pending coro=<main() running at D:/02-skills/python/500test/async_test.py:23> cb=[_run_until_complete_cb() at C:\python3\lib\asyncio\base_events.py:176]>
#<Task finished coro=<do_work() done, defined at D:/02-skills/python/500test/async_test.py:7> result='install mysql 6 done'>
    for ta in asyncio.Task.all_tasks():
        print(ta)

    for d in done:
        print(d.result())

if __name__ == '__main__':
    # main()
    loop=asyncio.get_event_loop()
    loop.run_until_complete(main())
    # for ta in task:
    #     print(ta.result())


