#coding=utf-8
"""
1.@classmethod:在类中运行，不用再实例中中运行
2.staticmethod
3.property
"""
class binary_bode(object):

    def __init__(self,left_ref,right_ref):
        self._left= left_ref
        self._right=right_ref

    #没有init函数
    @classmethod
    def _follow(cls,node,**kwargs):
        print('in _follow')
        return cls(left_ref=kwargs.get('left',node._left),
                   right_ref=kwargs.get('right', node._right))

    @property
    def addr(self):
        return self._left

    @addr.setter
    def addr(self,value):
        if value>10:  #主要作用就是这个
            raise 'value is large'
        self._left=value

class value_ref(object):
    def __init__(self):
        self._addr=1

class logicBase(object):
    node_ref_class=None
    value_ref=value_ref

    def __init__(self,storage):
        self._storage=storage

class binary_tree(logicBase):
    node_ref_class = binary_bode
    print('set node_ref_class')

    def _insert(self):
        pass

def test1():
    node=binary_bode(1,2)
    bnode=binary_bode._follow(node)
    print(type(bnode))
    print(node.addr)
    node.addr=3
    print(node.addr)

def test2():
    a='a'
    b_tree=binary_tree(a)
    b_tree.value_ref

if __name__=='__main__':
    #test1()
    test2()
