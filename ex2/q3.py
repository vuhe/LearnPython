from decimal import *

getcontext()
print(Decimal(1) / Decimal(7), end=' ')
getcontext().prec = 2
print(abs(Decimal(-3)), end='\n')
print(float(Decimal(-3)), end='\n')
