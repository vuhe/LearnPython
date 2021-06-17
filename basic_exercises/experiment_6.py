import json
import random
import string
from PIL import Image, ImageFilter


def question_2():
    f = open('./resources/data.txt', 'w+')
    for i in range(100):
        f.write(str(random.randint(1, 100)) + '\n')
    f.close()


def random_mac():
    """
    随机生成一个MAC地址
    """
    mac = '01-AF-3B'
    hex_num = string.hexdigits
    for i in range(3):
        n = random.sample(hex_num, 2)
        sn = '-' + ''.join(n).upper()
        mac += sn
    return mac


def creat_mac():
    """
    随机生成100个
    """
    with open('./resources/macAddr.txt', 'w+')as f:
        for i in range(100):
            mac = random_mac()
            f.write(mac + '\n')


def question_3():
    creat_mac()


def question_4():
    im = Image.open('./resources/上海.png')
    print(im.format, im.size, im.mode)

    om = im.filter(ImageFilter.CONTOUR)
    om.save('./resources/test.png')


def question_7():
    ls = [['姓名', '性别', '年龄', '班级'],
          ['张三', '男', '20', '18200'],
          ['李四', '女', '21', '17201'],
          ['王五', '女', '19', '19203'],
          ['候六', '女', '20', '18202']]

    fw = open('./resources/学生.csv', 'w')

    for row in ls:
        fw.write(",".join(row) + "\n")

    fw.close()


def question_8():
    fr = open("./resources/学生.csv", "r")
    ls = []
    for line in fr:
        line = line.replace('\n', '')
        ls.append(line.split(','))
    fr.close()
    for i in range(1, len(ls)):
        ls[i] = dict(zip(ls[0], ls[i]))

    print(json.dumps(ls[1:], indent=4, ensure_ascii=False))
