#!/usr/bin/python
#coding: utf-8
#@Author:liyichao
def base(*base_args):
    def warp():
        # base_args=base_args+1  #local variable 'base_args' referenced before assignment
        print(base_args)  #会包装成tutle对象
        sum=0
        for i in base_args: #这样可以执行
            sum+=i
        return sum
    return warp

def count_func():
    def warper():
        sum=0
        for i in range(1,4):
            sum+=i
        return sum
    warpers=[warper for i in range(0,3)]  #这样赋值是不对的，因为warper的值已经确定了
    return warpers

def count_func1():
    warpers=[]
    for i in range(1,4):
        def fun():
            return i*i
        warpers.append(fun)
    return warpers

def better_counter_func():
    w=[]
    def out(j):  #函数的主要功能，需要哪些参数，参数如何得来，返回那些参数--重构函数改写
        def ini():
            return j*j
        return ini

    for i in range(0,3):
        w.append(out(i))
    return w


def main():
    # f=base(1,2,3,4)
    # # f=base([1,2,3])  #传列表进去的做法是不对的
    # print(f())
    # f1,f2,f3 =count_func1()
    f1, f2, f3 = better_counter_func()
    print(f1())  #不要再闭包里面进行局部变量的循环
    print(f2())
    print(f3())

if __name__ == '__main__':
    main()
    
