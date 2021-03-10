input_str = input("请输入字符串：")
# 对称取字符判断
for i in range(len(input_str) // 2):
    # 遇到不一致字符退出判断
    if input_str[i] != input_str[-(i + 1)]:
        print('不', end='')
        break
print('是回文字符串')
