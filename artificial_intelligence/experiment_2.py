import numpy as np
from sklearn import linear_model

x = np.array(
    [[143], [145], [146], [147], [149], [150],
     [153], [154], [155], [156], [157], [158],
     [159], [160], [162], [164]])
y = np.array(
    [[88], [85], [88], [91], [92],
     [93], [93], [95], [96], [98],
     [97], [96], [98], [99], [100], [102]])

# 拟合
lr = linear_model.LinearRegression()
lr.fit(x, y)
k = lr.coef_[0][0]
b = lr.intercept_[0]

# 查看最佳拟合系数
print('y = ', k, 'x + ', b)
# 预测180
print('预测180腿长: ', k * 180 + b)
