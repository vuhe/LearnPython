# 利用递归函数调用方式，
# 将所输入的字符串中的字符，
# 以相反顺序打印出来
def reverse_print(input_str, curr=0):
    # 递归出口
    if len(input_str) == curr:
        return
    reverse_print(input_str, curr + 1)
    print(input_str[curr], end="")


reverse_print("1234567890")
