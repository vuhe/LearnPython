from datetime import datetime
import math
import turtle


def question_1():
    r = int(input("请输入圆的半径："))
    print("圆的面积是：", r ** 2 * math.pi)


def question_3():
    a, b = 0, 1
    while a < 1000:
        print(a, end=', ')
        a, b = b, a + b


def question_4():
    turtle.pensize(2)
    turtle.circle(10)
    turtle.circle(40)
    turtle.circle(80)
    turtle.circle(160)


def question_5():
    now = datetime.now()

    print(now, end='\n')
    print(now.strftime("%x"), end='\n')
    print(now.strftime("%X"), end='\n')


def question_6():
    str1 = input("第一个字符串：")
    str2 = input("第二个字符串：")

    print("输入的两个字符串是：{} 和 {}".format(str1, str2))


def question_7():
    n = input("请输入整数 N：")
    a_sum = 0
    for i in range(int(n)):
        a_sum += i + 1

    print("整数求和结果：", a_sum)


def question_8():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("{} * {} = {:2}".format(j, i, j * i), end=' ')
        print('\n')


def question_9():
    a_sum, tmp = 0, 1
    for i in range(1, 11):
        tmp *= i
        a_sum += tmp

    print("运算结果是：{}".format(a_sum))


def question_10():
    tem_str = input("请输入带符号的温度值：")
    tem_num = eval(tem_str[0:-1])
    if tem_str[-1] in ['F', 'f']:
        c = (tem_num - 32) / 1.8
        print("{}转换后的温度值是：{:.2f}C".format(tem_str, c))
    elif tem_str[-1] in ['C', 'c']:
        f = tem_num * 1.8 + 32
        print("{}转换后的温度值是：{:.2f}F".format(tem_str, f))
    else:
        print("输入的格式有误！")
