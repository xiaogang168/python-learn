#!/usr/bin/python
#coding: utf-8
#@Author:liyichao
import functools

def log(func):
    def wrapper(*args,**kargs):
        print('in wrapper')
        func(*args,**kargs)   #函数的参数传到这里执行
    return wrapper

#装饰器也需要参数的场景
def log(text):

    def middler(func):  #如需要传参，则需要包装两层
        def wrapper(*args,**kargs):
            print('in wrapper')
            print(text)
            func(*args,**kargs)
        return wrapper
    return middler

@log
def now():
    print('20180126')

@log('execute')
def now1():
    print('20180127')

def main():
    # now() #相当于执行 now=log(now)
    now1() # now1=log('excute')(now1)

if __name__ == '__main__':
    main()
    
