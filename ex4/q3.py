# 参数个数不限，
# 返回所有参数的乘积
def multi(*numbers) -> int:
    ans = 1
    for n in numbers:
        ans = ans * n
    return ans


print(multi(1, 2, 3, 4))
