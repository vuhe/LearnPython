#!/usr/bin/env python3

aSum, tmp = 0, 1
for i in range(1, 11):
    tmp *= i
    aSum += tmp

print("运算结果是：{}".format(aSum))
