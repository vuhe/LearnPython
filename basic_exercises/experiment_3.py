import time
from random import *
import numpy as np
import matplotlib.pyplot as plt


def question_1():
    # 初始化生成器
    seed()
    # 返回给定范围内的随机数
    print(randrange(-10, 8))
    # 返回给定范围内的随机数
    print(randint(0, 20))
    # 返回给定序列的随机元素
    print(choice([1, 2, 5, 3, 5, 7]))
    # 返回序列的给定样本
    print(sample([1, 2, 3, 5, -4, 'ss'], 3))
    # 返回 0～1 的浮点数
    print(random())
    # 返回两个给定参数之间的随机浮点数
    print(uniform(1, 2))
    # 返回两个给定参数之间的随机浮点数，指定 mode
    print(triangular(0.2, 0.9, mode=0.4))
    x = [1, 2, 3, 4]
    # 打乱序列
    shuffle(x)
    print(x)


def question_2():
    for s in "PYTHON":
        if s == "T":
            continue
        print(s, end="")
    print()

    for s in "PYTHON":
        if s == "T":
            break
        print(s, end="")
    print()

    for s in "BIT":
        for i in range(10):
            print(s, end="")
            if s == "I":
                break


def question_3():
    # 作用是格式化时间戳为本地的时间
    print(time.localtime())
    # 作用是格式化时间戳为本地的时间
    print(time.asctime())
    time.sleep(2 + 3)
    # 作用是格式化时间戳为本地的时间
    print(time.ctime())
    # 1970纪元后经过的浮点秒数
    print(time.time())
    print(time.process_time() / time.process_time_ns())


def question_4():
    # 单分支
    s = eval(input("请输入一个整数："))
    if s % 2 == 0:
        print("这是个偶数")
    print("输入的数字是：", s)

    # 二分支
    if True:
        print("语句1")
    else:
        print("语句2")

    # 紧凑形式：用于表达简单地二分支结构
    guess = eval(input())
    print("猜{}了".format("对" if guess == 99 else "错"))

    # 多分支
    if True:
        print("1")
    elif True:
        print("2")
    else:
        print("3")


def question_6():
    try:
        raise IOError
    except IOError:
        print("IOError")

    try:
        raise SystemExit
    except SystemExit:
        print("SystemExit")

    try:
        raise OverflowError
    except OverflowError:
        print("OverflowError")

    try:
        raise EOFError
    except EOFError:
        print("EOFError")


def f(x0) -> int:
    return x0 ** 2


def question_7():
    """
    蒙特卡罗方法求函数 y=x^2 在[0,1]内的定积分（值）
    """

    # 投点次数
    n = 10000

    # 矩形区域边界
    x_min, x_max = 0.0, 1.0
    y_min, y_max = 0.0, 1.0

    # 在矩形区域内随机投点
    x = np.random.uniform(x_min, x_max, n)  # 均匀分布
    y = np.random.uniform(y_min, y_max, n)

    # 统计 落在函数 y=x^2图像下方的点的数目
    res = sum(np.where(y < f(x), 1, 0))

    # 计算 定积分的近似值（Monte Carlo方法的精髓：用统计值去近似真实值）
    integral = res / n

    print('integral: ', integral)

    # 画个图看看
    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.plot(x, y, 'ro', markersize=1)
    plt.axis('equal')  # 防止图像变形

    axes.plot(np.linspace(x_min, x_max, 10), f(np.linspace(x_min, x_max, 10)), 'b-')  # 函数图像

    plt.show()
