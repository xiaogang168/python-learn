#!/usr/bin/python
#coding: utf-8
#@Author:liyichao
class base(object):
    def __init__(self):
        pass

class single(object):
    # _single=None  #可以再这里设置环境变量，表示不再进行__init__进行初始化
    # a=1
    def __init__(self,*args,_b='c',**kwargs):
        # self._single=None
        # print(args)
        # print(kwargs)
        # self.a=2
        pass
    # def getInstance(self):  #这种方法不好，需要创建实例之后再实例里面调用才行
    #     if self._single:
    #         return self._single
    #     else:
    #         self._single=single
    #         return self._single

    @classmethod
    def getInstance(cls):  #实现方法是一样的
        # cls._single=None  #这个变量是一个局部变量
        if hasattr(cls,'_single'):  #通过这种方式查看类是否有变量，前面是object,后面是属性。
            # 注意，object也可以是一个包，用于实现“反射”
            return cls._single
        else:
            cls._single=cls()
            return cls._single

    # @staticmethod
    # def getInstance():
    #     #s._single=None  #这个需要找一个能够在内里面存在的变量判断是否存在
    #     if _single:
    #         return _single
    #     else:
    #         _single=single()
    #         return _single

    # def __new__(cls,*args,**kwargs):
    #     if hasattr(cls,'_single'):
    #         return cls._single
    #     else:
    #         cls._single=super().__new__(cls, *args, **kwargs)
    #         return cls._single

def main():
    # a=base()
    # b=base()  #不同的对象
    # print(a,b)
    # assert a==b
    # a=single()
    # b=single()
    # print(a.a)
    # # a.a=2
    # print(b.a)
    # print(a,b)
    a=single.getInstance()
    b=single.getInstance()
    assert a==b

if __name__ == '__main__':
    main()
    
