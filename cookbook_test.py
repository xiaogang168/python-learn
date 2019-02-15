#!/usr/bin/python
#coding: utf-8
#@Author:liyichao

class A(object):
    def __init__(self):
        self.fun_locals=None
        self.fun_global=None
    def fun(self):
        self.fun_locals=locals()
        self.fun_global=globals()



def main():
    # Lo=locals()
    # Go=globals()
    # Vo=vars()
    # print(Lo)
    # print(Go)
    # print(Vo)

    a = A()
    a.fun()
    a_vars=vars(a)
    print(vars(a))  #返回__dict__属性
    print(vars(A))
    a_vars['func_vars'] = "vars"
    print(a.func_vars)



if __name__ == '__main__':
    main()
    
