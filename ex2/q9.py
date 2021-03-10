input_str = input("请输入字符串：")
for i in range(len(input_str) // 2):
    if input_str[i] != input_str[-(i + 1)]:
        print('不', end='')
        break
print('是回文字符串')
