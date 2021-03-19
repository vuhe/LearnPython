from random import *

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
