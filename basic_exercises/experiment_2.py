import math
import random
import sys
# 精确计算模块
from decimal import *


def question_1():
    # python目录
    print(sys.executable, end='\n')
    # 运行路径
    print(sys.path, end='\n')
    # 运行平台
    print(sys.platform, end='\n')
    # 运行版本
    print(sys.version, end='\n')
    # 默认编码
    print(sys.getdefaultencoding(), end='\n')


def print_type(a):
    print(type(a), end='\n')


def question_2():
    # 输出所有类型
    print_type(1)
    print_type(1.0)
    print_type('')
    print_type('a')
    print_type('ab')
    print_type("ab")
    print_type('''ab''')
    print_type(3 + 4j)
    print_type([])
    print_type([1, 2])
    print_type((1, 2))
    print_type(range(5))
    print_type(divmod(5, 2))


def question_3():
    getcontext()
    # 取除数
    print(Decimal(1) / Decimal(7), end=' ')
    getcontext().prec = 2
    # 取绝对值
    print(abs(Decimal(-3)), end='\n')
    # 取浮点值
    print(float(Decimal(-3)), end='\n')


def question_4():
    # 除法，除不尽时为小数
    print(5 / 3, end=' ')
    # 整除，除不尽时舍余数
    print(5 // 3)
    # 取余
    print(5 % 3, end=' ')
    # 乘法
    print(5 * 3, end=' ')
    # 乘方
    print(5 ** 3)


def question_5():
    # 转为 int 类型
    print(int('3'), end=' ')
    # 转为 float 类型
    print(float('4.5'), end=' ')
    # 转为 复数 类型
    print(complex(real=1, imag=5), end=' ')
    # 转为 string 类型
    print(str(20))
    # 转为 boolean 类型
    print(bool('true'), end=' ')
    # 取 十六进制 值
    print(hex(10), end=' ')
    # 取 二进制 值
    print(bin(10))


def question_6():
    # x 的向上取整，即大于或者等于 x 的最小整数
    print(math.ceil(2.5))
    # 返回不重复且无顺序地从 n 项中选择 k 项的方式总数
    print(math.comb(4, 2))
    # 返回一个基于 x 的绝对值和 y 的符号的浮点数
    print(math.copysign(1.0, -0.0))
    # 返回 x 的绝对值
    print(math.fabs(-2))
    # x 的向下取整，小于或等于 x 的最大整数
    print(math.floor(2.5))
    # 返回 x 的正弦值
    print(math.sin(0))


def question_7():
    # 返回原字符串的副本，其首个字符大写，其余为小写
    print(str.capitalize('vuhe'), end=' ')
    # 返回原字符串消除大小写的副本
    print(str.casefold('Vuhe'), end=' ')
    # 如果字符串中的所有字符都是字母或数字且至少有一个字符，
    # 则返回 True ， 否则返回 False
    print(str.isalnum('vuhe1'))
    # 如果字符串中的所有字符都是字母，并且至少有一个字符，
    # 返回 True ，否则返回 False
    print(str.isalpha('vuhe1'), end=' ')
    # 返回原字符串的副本，其所有区分大小写的字符均转换为小写
    print(str.lower('VUHE'), end=' ')
    # 返回原字符串的副本，其所有区分大小写的字符均转换为大写
    print(str.upper('vuhe'))


def question_8():
    # 生成随机数
    number = random.randint(0, 10)
    # 循环判断
    while True:
        n = int(input("请输入你猜的数字："))
        if n == number:
            print('猜对了！')
            break
        elif (n - number) > 0:
            print('大了')
        else:
            print('小了')


def question_9():
    input_str = input("请输入字符串：")
    # 对称取字符判断
    for i in range(len(input_str) // 2):
        # 遇到不一致字符退出判断
        if input_str[i] != input_str[-(i + 1)]:
            print('不', end='')
            break
    print('是回文字符串')
