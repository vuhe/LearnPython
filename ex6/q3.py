import string
import random


# 随机生成一个MAC地址
def random_mac():
    mac = '01-AF-3B'
    hex_num = string.hexdigits
    for i in range(3):
        n = random.sample(hex_num, 2)
        sn = '-' + ''.join(n).upper()
        mac += sn
    return mac


# 随机生成100个
def creat_mac():
    with open('./resources/macAddr.txt', 'w+')as f:
        for i in range(100):
            mac = random_mac()
            f.write(mac + '\n')


creat_mac()
