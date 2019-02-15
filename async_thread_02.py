#coding:utf-8
from threading import Thread
import asyncio
import time
now = lambda: time.time()

#串行执行的例子
def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

def more_work(x):
    print('More work {}'.format(x))
    time.sleep(x)
    print('Finished more work {}'.format(x))

start = now()
new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()
print('TIME: {}'.format(time.time() - start))

new_loop.call_soon_threadsafe(more_work, 6) #接受callback即可
new_loop.call_soon_threadsafe(more_work, 3)  #每个more worker串行执行







