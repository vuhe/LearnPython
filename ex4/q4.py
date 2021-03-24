import math


# 参数为整数，要有异常处理。
# 如果整数是质数，返回True，否则返回False
def is_prime(n) -> bool:
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


print(is_prime(37))
