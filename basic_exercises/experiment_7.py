from matplotlib import pyplot as plt
from matplotlib.pyplot import *


def question_1():
    # 初始化
    x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)

    # 数组属性
    print(x.flags)
    print(x.size, end=" ")
    print(x.shape, end=" ")

    print(x.dtype)


def question_2():
    # 数学
    a = np.array([0, 30, 45, 60, 90])
    print('含有正弦值的数组：', np.sin(a * np.pi / 180), end='\n\n')

    # 算数
    a = np.arange(9, dtype=np.float_).reshape(3, 3)
    b = np.array([10, 10, 10])
    print('两个数组相加：', np.add(a, b), end='\n\n')

    # 统计
    a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
    print('调用 amin() 函数：', np.amin(a, 1), end='\n\n')

    # 矩阵及运算
    a = np.arange(12).reshape(3, 4)
    print('原数组：', a)
    print('转置数组：', a.T, end='\n\n')

    # 线性代数运算
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[11, 12], [13, 14]])
    print(np.dot(a, b))


def question_3():
    # 绘制饼图
    n = 20
    z = np.random.uniform(0, 1, n)
    pie(z), show()

    # 直方图
    fig, ax = plt.subplots(1, 1)
    a = np.array([22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27])
    ax.hist(a, bins=[0, 25, 50, 75, 100])
    ax.set_xticks([0, 25, 50, 75, 100])
    show()

    # 散点图
    n = 1024
    x = np.random.normal(0, 1, n)
    y = np.random.normal(0, 1, n)
    scatter(x, y)
    show()

    # 条形图
    n = 12
    x = np.arange(n)
    y1 = (1 - x / float(n)) * np.random.uniform(0.5, 1.0, n)
    y2 = (1 - x / float(n)) * np.random.uniform(0.5, 1.0, n)
    bar(x, +y1, facecolor='#9999ff', edgecolor='white')
    bar(x, -y2, facecolor='#ff9999', edgecolor='white')
    for x_, y_ in zip(x, y1):
        text(x_ + 0.4, y_ + 0.05, '%.2f' % y_, ha='center', va='bottom')
    ylim(-1.25, +1.25)
    show()

    # 柱状图
    data = [5, 20, 15, 25, 10]
    plt.bar(range(len(data)), data)
    plt.show()


def question_4():
    # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
    figure(figsize=(8, 6), dpi=80)
    # 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
    subplot(1, 1, 1)
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    c, s = np.cos(x), np.sin(x)

    # 标注
    ax = gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

    # 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
    plot(x, c, color="blue", linewidth=1.0, linestyle="-")
    # 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
    plot(x, s, color="red", linewidth=1.0, linestyle="-")

    # 图例
    legend(loc='upper left')
    # 注释
    t = 2 * np.pi / 3
    plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
    scatter([t, ], [np.cos(t), ], 50, color='blue')

    annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    plot([t, t], [0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
    scatter([t, ], [np.sin(t), ], 50, color='red')

    annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    # 设置横轴的上下限
    xlim(-4.0, 4.0)
    # 设置横轴记号
    xticks(np.linspace(-4, 4, 9, endpoint=True))
    # 设置纵轴的上下限
    ylim(-1.0, 1.0)
    # 设置纵轴记号
    yticks(np.linspace(-1, 1, 5, endpoint=True))

    # 在屏幕上显示
    show()
