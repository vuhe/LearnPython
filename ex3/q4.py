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
