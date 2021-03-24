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
