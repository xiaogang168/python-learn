#四舍五入
round(1.23, 1)
round(12673, -1) #舍去最后一位的精度
format(1.123, '0.2f')

#精确浮点数运算
from decimal import Decimal
from decimal import localcontext
import math
a = Decimal('4.2')
b = Decimal('2.1')
(a+b) ==Decimal('6.3')
nums = [1.23e+18, 1, -1.23e+18]  #浮点数相加
math.fsum(nums)

#不同进制的数字
print(bin(x), oct(x), hex(x))
print(int('4d2', 16)) #转换回去



