import math
import datetime as dt
from numbers import Number


def is_odd(x) -> bool:
    """
    参数为整数，如果整数位奇数，
    返回True，否则返回False
    """
    return x & 1 == 1


def question_1():
    print(is_odd(1))
    print(is_odd(2))


def is_num(n) -> bool:
    """
    参数为一个字符串，
    如果这个字符串属于整数、浮点数或复数表示，
    则返回True，否则返回False
    """
    n = eval(n)
    # 类型判断
    if isinstance(n, Number):
        return True
    else:
        return False


def question_2():
    print(is_num(input("输入：")))


def multi(*numbers) -> int:
    """
    参数个数不限，
    返回所有参数的乘积
    :param numbers:
    :return:
    """
    ans = 1
    for n in numbers:
        ans = ans * n
    return ans


def question_3():
    print(multi(1, 2, 3, 4))


def is_prime(n) -> bool:
    """
    参数为整数，要有异常处理。
    如果整数是质数，返回True，否则返回False
    """
    try:
        # 异常处理
        if not isinstance(n, int):
            assert ValueError
        # 运算
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    except ValueError:
        print("输入有误")


def question_4():
    print(is_prime(37))


def reverse_print(input_str, curr=0):
    """
    利用递归函数调用方式，
    将所输入的字符串中的字符，
    以相反顺序打印出来
    """
    # 递归出口
    if len(input_str) == curr:
        return
    reverse_print(input_str, curr + 1)
    print(input_str[curr], end="")


def question_5():
    reverse_print("1234567890")


def question_6():
    # 把作为参数传入的 x, y 相加
    print((lambda x, y: x + y)(2, 3), end=" ")
    # 把作为参数传入的 x, y, z 相加
    print((lambda x, y, z=3: x + y + z)(1, 2), end=" ")
    # 把作为传入的可变参数相加
    print((lambda *args: sum(args))(1, 2, 3), end=" ")

    # 把入参 + 传入的函数返回值
    high_ord_func = lambda x, func: x + func(x)
    # 定义入参和传入的 lambda 函数
    print(high_ord_func(2, lambda x: x * x))


def question_7():
    # 获取当前datetime
    now = dt.datetime.now()
    print(now)

    d = dt.date(2021, 3, 24)
    print(d)
    # 打印年
    print('year:', d.year)
    # 打印月
    print('month:', d.month)
    # 打印日
    print('day:', d.day)


def question_8():
    a = {1, 2, 3, 4, 5}
    b = {2, 3, 4, 5, 6}

    # 求并集
    print(a.union(b))

    # 随机返回一个元素
    print(a.pop())
