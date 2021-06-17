from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


def read_data():
    """
    读取txt文件中的数据
    :return: 将数据转换为向量
    """
    file = open("./resources/data.txt", "r")
    line = file.readline()
    y, x = [], []
    while line:
        line = file.readline()
        # 通过空格分割
        line1 = line.split()
        if line1:
            y.append(int(line1[0]))
            x.append([float(line1[1]), float(line1[2]), float(line1[3])])
    file.close()
    return y, x


def train(x, y):
    # 将数据集划分为训练集和测试集，其中70%为训练集，30%为测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.6, random_state=0)
    sc = StandardScaler()
    # 通过fit方法，可以计算训练集中样本均值和方差
    sc.fit(x_train)
    # 通过transform方法，进行标准化处理
    x_train_std = sc.transform(x_train)
    x_test_std = sc.transform(x_test)

    # logistic回归
    lr = LogisticRegression(C=100.0, random_state=0)
    lr.fit(x_train_std, y_train)
    print(lr)
    # 返回准确度
    print("Training Score: ", lr.score(x_train_std, y_train))
    print("Testing Score:  ", lr.score(x_test_std, y_test))


Y, X = read_data()
train(X, Y)
