#!/usr/bin/env python3

temStr = input("请输入带符号的温度值：")
temNum = eval(temStr[0:-1])
if temStr[-1] in ['F', 'f']:
    c = (temNum - 32) / 1.8
    print("{}转换后的温度值是：{:.2f}C".format(temStr, c))
elif temStr[-1] in ['C', 'c']:
    f = temNum * 1.8 + 32
    print("{}转换后的温度值是：{:.2f}F".format(temStr, f))
else:
    print("输入的格式有误！")
