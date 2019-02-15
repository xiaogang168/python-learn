#关键字参数
def recv(maxsize, *, block):
    'Receives a message'
    pass
# recv(1024, True) # TypeError
recv(1024, block=True)  # Ok
def minimum(*values, clip=None):  #会形成一个元组
    m = min(values)
minimum(1, 5, 2, -5, 10) 

#闭包 
def urltemplate(template):
    sequence = 0
    def opener(**kwargs):
        nonlocal sequence
        return urlopen(template.format_map(kwargs))
    return opener
yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))
#如上也可以包装成类实现
class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))
yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))

#回调函数
#可以使用闭包、类或者协程实现
"""
协程两方：yield循环，保存私有变量  （消费者）
send或者next, 以消费者实例为参数，生产者（通知消费者）
r=send(n) 发送参数n,接受参数r
n=yield(r) 接受参数n,发送参数r
"""
def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

handler = make_handler()
next(handler) # Advance to the yield
apply_async(add, (2, 3), callback=handler.send)
apply_async(add, ('hello', 'world'), callback=handler.send)

#










