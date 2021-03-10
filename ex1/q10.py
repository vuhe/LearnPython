tem_str = input("请输入带符号的温度值：")
temNum = eval(tem_str[0:-1])
if tem_str[-1] in ['F', 'f']:
    c = (temNum - 32) / 1.8
    print("{}转换后的温度值是：{:.2f}C".format(tem_str, c))
elif tem_str[-1] in ['C', 'c']:
    f = temNum * 1.8 + 32
    print("{}转换后的温度值是：{:.2f}F".format(tem_str, f))
else:
    print("输入的格式有误！")
