#!/usr/bin/python
#coding: utf-8
#@Author:liyichao
from collections import defaultdict
"""
1.统计列表中重复的元素数量
2.实现[(,), (,)]类似groupBy效果

"""
class base():
    def main(self):
        raise 'no implement'

class testdict(base):
#{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
    @staticmethod  #不需要实例化就可以执行的函数
    def main():
        s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
        d = defaultdict(list)
        for k, v in s:
            d[k].append(v)
        print(d.items())  #将dict转换成列表,items ((key, value) pairs)
        print(sorted(d.items()))  #将
        print(d) #排序之后不会变化

class testset(base):
#{'yellow': {1, 3}, 'blue': {2, 4}, 'red': {1}}
    def main(self):
        s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
        d=defaultdict(set)
        for k, v in s:
            d[k].add(v)  #set是这个方法
        print(d.items())  #将dict转换成列表
        print(sorted(d.items()))  #将
        print(d) #排序之后不会变化

class testdict_1(base):
    def main(self):
        #上面等效下面的设置
        d = {}
        s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
        for k, v in s:
            d.setdefault(k, []).append(v)

class testint(base):
    def main(self):
        #还有一种用法，设置计数器
        s = 'mississippi'
        d = defaultdict(int)  #默认值为0
        for k in s:
            d[k] += 1
        sorted(d.items())

#实现类似计数的功能
from collections import Counter
c=Counter()
for ch in c:
    c[ch]+=1

if __name__ == '__main__':
    # testdict=testdict()
    testdict.main()
    
