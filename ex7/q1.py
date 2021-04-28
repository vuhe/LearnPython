import numpy as np

# 初始化
x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)

# 数组属性
print(x.flags)
print(x.size, end=" ")
print(x.shape, end=" ")

print(x.dtype)
