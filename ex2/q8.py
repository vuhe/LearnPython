import random

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
