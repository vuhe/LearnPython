# 参数为整数，如果整数位奇数，
# 返回True，否则返回False
def is_odd(x) -> bool:
    return x & 1 == 1


print(is_odd(1))
print(is_odd(2))
