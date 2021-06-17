from typing import Dict

from matplotlib import pyplot as plt


def draw_result(dic: Dict[str, int]):
    x, y = [], []
    for department, count in dic.items():
        x.append(department)
        y.append(count)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.barh(x, y, color='blue', alpha=1.0)
    plt.title('部门出现频率统计')
    plt.xlabel('部门')
    plt.ylabel('频率')
    plt.show()
