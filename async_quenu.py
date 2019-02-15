import asyncio
from asyncio import Queue
import time
"""
使用quenue的一个例子，两个队列，一个生产者队列，一个消费者队列
使用的方法包括：

"""
class aTest_01:
    def __init__(self):
         self.que = Queue()
         self.pue = Queue()
    async def consumer(self):
        print("enter in consume")
        while True:
            try:
             print('consumer',await self.que.get())
            finally:
                try:
                    self.que.task_done()
                except ValueError:
                    if self.que.empty():
                        print("que empty")
        print("out of test")  #不会执行这一段，当抛出异常之后，协程就结束了

    async def work(self):
        print("enter to work")
        while True:  #什么时候退出循环？
            try:
                value = await self.pue.get()
                print('producer', value)
                await self.que.put(value)
                #print(self.que)
            finally:
                try:
                    self.pue.task_done()  #the processing on the task is complete.
                    print(self.pue)
                except ValueError:
                    if self.pue.empty():
                        print("pue empty")
        print("out of work")

    async def suplent(self):  #需要注册到tasks中执行
        print("enter in suplent")
        value=await self.que.get()
        print('suplent',value)

    async def run(self):
        await asyncio.wait([self.pue.put(i)for i in range(10)])  #wait可以获取一个协同程序的列表，同时返回一个将它们
        # 全包括在内的单独的协同程序
        print(self.pue)
        tasks = [asyncio.ensure_future(self.work())]
        tasks.append(asyncio.ensure_future(self.consumer())) #两个方法也是串行的
        print('p queue join')
        # await self.pue.join()  #两个队列，只需要这个队列join之后即可完成写成的调用，该队列的数据执行完毕之后，解除阻塞
        await asyncio.sleep(2)   #join只是用于等待队列执行完毕，使用await释放cpu，一样可以等待task任务执行完毕
        print('p queue is done & q queue join') #阻塞了当前的进程，所以这一段在最后才会执行
        #await self.que.join()  #q虽然没有数据，但是仍然能够进入到consume任务
        print('q queue is done')
        for task in tasks:
            task.cancel()  #执行完毕之后，取消任务

if __name__ =='__main__':
     print('----start----')
     case = aTest_01()
     loop = asyncio.get_event_loop()
     loop.run_until_complete(case.run())
     print('----end----')
