#并发任务执行
#1.主从模式，主线程中有一个是无限循环，用户消费队列。子线程处理
#2.子进程消费，处理

# Example of the queue how to work
import asyncio
from asyncio import Queue

async def work(q):
    while True:
        i = await q.get()
        print(q.qsize()) #执行完毕之后不会有异常出来
        #q.task_done()
        try:
            print(i)
            print('q.qsize(): ', q.qsize())
        finally:
            q.task_done()  ##一定要执行这个才算是把队列里面的任务完成了

async def run():
    q = Queue()
    await asyncio.wait([q.put(i) for i in range(10)])
    print(q)  #等待上面的异步完成完毕，由于是异步，存放的在q的顺序也不一样
    #try:
    tasks = [asyncio.ensure_future(work(q))]  #只有一个协程异步执行，循环消费队列
    print('wait join')
    await q.join()  #开始执行task任务，队列被消费完毕之后才会推出
    print('end join')
    for task in tasks:
        task.cancel() #
#except KeyboardInterrupt as e:  #这一段无法捕捉异常，原因？
    #print(e)
    # loop.stop()
    # loop.run_forver()
#finally:
    #loop.close()

if __name__ =='__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.stop() #与close差别
    loop.close()
