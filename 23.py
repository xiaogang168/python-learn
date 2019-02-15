#!/usr/bin/python
#coding: utf-8
#@Author:liyichao
from collections import defaultdict

def log_missing():
    print('miss key')
    return 0

def hooks():
    current={'green':1,'red':2}
    increments=[('blue',3),('orange',4)]
    count=0

    #使用闭包
    def missing():
        nonlocal count
        print('miss key')
        count += 1
        return 0

    result=defaultdict(missing, current)  #使用闭包，函数保存了count的状态

    # result=defaultdict(log_missing,current)
    for key,amount in increments:
        result[key]+=amount
    print(dict(current))

    print(count)
    assert count==2

#使用类保存进程内部状态
class CountMissing(object):
    def __init__(self):
        self.count=0
    def missing(self):
        self.count+=1
        return 0

#实现方式二
def hook2():
    countmiss=CountMissing()
    current={'green':1,'red':2}
    increments=[('blue',3),('orange',4)]
    result=defaultdict(countmiss.missing,current)
    for key,amount in increments:
        result[key]+=amount
    print(dict(current))
    print(countmiss.count)

#实现方式三
class BetterCountMissing(object):
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return 0

#实现方式二
def hook3():
    counter=BetterCountMissing()
    counter()  #会调用__call__函数
    print(counter.count)
    assert callable(counter)
    print(counter.count)

    current={'green':1,'red':2}
    increments=[('blue',3),('orange',4)]
    result=defaultdict(counter,current)  #直接使用类实例,__call__可以当成
    for key,amount in increments:
        result[key]+=amount
    print(dict(current))
    print(counter.count)

def main():
    # hooks()
    hook3()

if __name__  == '__main__':
    main()
