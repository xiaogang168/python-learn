#!/usr/bin/python
#coding: utf-8
#@Author:liyichao
"""
这一章是各种数据结构的使用范例。
主要的内容有：
"""
def main():

#只有字典有这个，列表不能这样操作，与、或、求反
#列表求交并集，需要转换成set，set支持& | - ^ 格式
    print('Common keys:', a.keys() & b.keys())
    print('Keys in a not in b:', a.keys() - b.keys())
    print('(key,value) pairs in common:', a.items() & b.items())

#筛选出现自定的元素
    from itertools import compress
    a = list(compress(addresses, more5))

#返回列表次数出现最高的几个元素
    from collections import Counter
    word_counts = Counter(words)
    top_three = word_counts.most_common(3) #返回列表类型元素
    morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
    word_counts.update(morewords) #还可以直接更新

    x, y = zip([1, 2], [3, 4])
    x, y = zip(*zip([1, 2, 3], [4, 5, 6]))  #反向 x=(1,2,3)

#打印字典key最大的几个值
    min_price = min(zip(prices.keys(), prices.values())) #mina函数可以比较元祖的首个元素
    max_price = max(zip(prices.values(), prices.keys()))
    #sorted(iterable, key=keyfunc, reverse=True)[0]  keyfunc接受1个参数，比较返回值，当多个参数，使用偏函数
    #heapq.nlargest(1, iterable, key=keyfunc)  #找到最大的几个值  import heapq
    prices_sorted = sorted(zip(prices.values(), prices.keys())) #排序


#实现group by方法
    from itertools import groupby
    rows.sort(key=lambda r: r['date']) #首先需要将列表中按照key排序
    for date, items in groupby(rows, key=lambda r: r['date']):
        print(date)
        for i in items:
            print('    ', i)
    #方法二
    from collections import defaultdict
    rows_by_date = defaultdict(list)
    for row in rows:
        rows_by_date[row['date']].append(row)

#实现股票分红计算
    from collections import namedtuple
    Stock = namedtuple('Stock', ['name', 'shares', 'price'])
    records = [
        ('GOOG', 100, 490.1),
        ('ACME', 100, 123.45),
        ('IBM', 50, 91.15)
    ]
    for rec in records:
        s = Stock(*rec)

#获取最近五行数据
    def search(lines, pattern, history=5):
        previous_lines = deque(maxlen=history) # from collections import deque
        for line in lines:
            if pattern in line:
                yield line, previous_lines
            previous_lines.append(line)
#heap合并
    heapA = [random.randrange(1,100) for _ in range(3)]
    heapB = [random.randrange(1,100) for _ in range(3)]
    merged(heapA,heapB)
    heapqpushpop(l,i)
    heapreplace(l, i)

#优先队列,
# list pop()从尾部弹出元素
#向heapq中插入元组，元素弹出按照最小开始
    class PriorityQueue:
        def __init__(self):
            self._queue = []
            self._index = 0

        def push(self, item, priority):
            #heap.nlargest(n, iterable[, key])
            #heap.nsmallest(n, iterable[, key])
            #heapq.heapitf(l) 列表转换成堆
            heapq.heappush(self._queue, (-priority, self._index, item))
            self._index += 1

        def pop(self):
            return heapq.heappop(self._queue)[-1]

#移除重复值，但保持顺序
    #列表
    def dedupe(items):
        seen = set()  #直接这样会自动排序
        for item in items:
            if item not in seen:
                yield item
                seen.add(item)
    #字典
    def dedupe(items, key=None):  #key=lambda a: (a['x'],a['y'])  转换成tuple
        seen = set()
        for item in items:
            val = item if key is None else key(item)
            if val not in seen:
                yield item
                seen.add(val)

#根据字典中公共的keys进行排序
    from operator import itemgetter
    rows_by_fname = sorted(rows, key=itemgetter('fname'))

#找到类中的keys进行排序
    from operator import attrgetter
    print(sorted(users, key=attrgetter('user_id')))

#注意这种for循环的形式
    for tag, *args in records:
        pass

#itertools
    def tools():
        count(10,1)  #会一致执行下去
        itertools.repeat(10,3)
        chain() #
        imap() ##与map不同，可以对无穷队列做map
        from collections import ChainMap
        compress('abcde',[1,0,1,0,1])
        dropwhile(predicate, iterable) #predicate(item)为True,则丢弃
        ifilter(predicate, iterable) #predicate(item)为True,则保留
        

if __name__ == '__main__':
    main()
    
