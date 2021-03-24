from numbers import Number


# 参数为一个字符串，
# 如果这个字符串属于整数、浮点数或复数表示，
# 则返回True，否则返回False
def is_num(n) -> bool:
    n = eval(n)
    # 类型判断
    if isinstance(n, Number):
        return True
    else:
        return False


print(is_num(input("输入：")))
