#!/usr/bin/python
#coding: utf-8
#@Author:liyichao
import random
#简单工厂
class chinaese():
    pass
class english():
    pass

def simplefactory(language):
    _fac=dict(chinaese=chinaese,english=english) #可以直接用类名代替
    print(_fac)
    return _fac[language]()

#抽象工程
class chinafactory():
    pass  #返回chinaese
class englandfactory():
    pass

class countryfactory():
    def __init__(self):
        self.fac=None #作为保存country的地方

    def show(self):
        pass  #执行country方法

    @staticmethod
    def getfactory():
        return random.choices([chinafactory,englandfactory])()



def main():
    # sf=simplefactory('english')
    # print(sf)
    cf=countryfactory()
    cf.fac=countryfactory.getfactory()
    cf.show()

if __name__ == '__main__':
    main()
    
