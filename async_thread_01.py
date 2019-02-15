#coding:utf-8
from threading import Thread
import asyncio
import time
now = lambda: time.time()

#将子进程里面设置循环，协程函数注册到循环中，并行执行，
# 无法执行退出,子线程无法捕获异常，无法退出
def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

async def do_some_work(x):
    print('Waiting {}'.format(x))
    await asyncio.sleep(x)
    print('Done after {}s'.format(x))
    raise 'do_some_work $d dome'%x

def more_work(x):
    print('More work {}'.format(x))
    time.sleep(x)
    print('Finished more work {}'.format(x))

start = now()
new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
# t.setDaemon(True)  #子线程设为守护线程，子线程结束后，主线程也结束了
t.start()
print('TIME: {}'.format(time.time() - start))

try:
    asyncio.run_coroutine_threadsafe(do_some_work(1), new_loop)  #接受协程
    asyncio.run_coroutine_threadsafe(do_some_work(2), new_loop)
    # new_loop.close()  #针对run_until_complete调用的时候
    # new_loop.stop()  #在这里执行会报错：Task was destroyed but it is pending!

    # for task in asyncio.Task.all_tasks():
    #     print(task.cancle())
    # new_loop.stop()

    # done pending=new_loop.
except KeyboardInterrupt as e:
    print(e)
    new_loop.stop()
finally:
    # new_loop.call_soon_threadsafe(do_some_work(1).cancel)
    # new_loop.call_soon_threadsafe(do_some_work(2).cancel)
    pass
