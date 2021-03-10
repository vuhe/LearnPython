# 精确计算模块
from decimal import *

getcontext()
# 取除数
print(Decimal(1) / Decimal(7), end=' ')
getcontext().prec = 2
# 取绝对值
print(abs(Decimal(-3)), end='\n')
# 取浮点值
print(float(Decimal(-3)), end='\n')
