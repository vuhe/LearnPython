from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

# 加载数据
iris = load_iris()
# 分割数据集
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.25)

# 特征工程标准化
std = StandardScaler()
x_train = std.fit_transform(x_train)
x_test = std.transform(x_test)

# knn 算法
knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
y_predict = knn.predict(x_test)

# 结果
labels = ["山鸢尾  ", "虹膜锦葵", "变色鸢尾"]
for i in range(len(y_predict)):
    print("%d\t真值: %s\t预测: %s" % ((i + 1), labels[y_predict[i]], labels[y_test[i]]))
print("准确率: ", knn.score(x_test, y_test))
