#!/usr/bin/python
#coding: utf-8
#@Author:liyichao
import asyncio
"""
异步大循环一定是多任务的才需要异步，单个任务没有意义
使用asyncio建立server函数
"""
@asyncio.coroutine
def wget(host):
    connect=asyncio.open_connection(host,80)
    reader,writer=yield from connect
    header='GET /HTTP/1.0\r\nHost:%s\r\n\r\n'%host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line=yield from reader.readline()
        if line==b'\r\n':
            break
        print('done')
    writer.close()

def main():
    loop=asyncio.get_event_loop()
    tasks=[wget(host) for host in ['www.baidu.com','www.sina.com']]
    loop.run_until_complete(asyncio.wait(tasks)) #wait需要接受协程对象，可以使用列表封装
    loop.close()


if __name__ == '__main__':
    main()
    
