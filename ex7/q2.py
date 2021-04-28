import numpy as np

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
