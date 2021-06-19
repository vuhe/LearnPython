import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 禁用log
import tensorflow as tf
from tensorflow.keras import *
import matplotlib.pyplot as plt

# 网络加载
network = models.load_model('./mnist_data/model.h5')
network.summary()

# 读取数据集
mnist = tf.keras.datasets.mnist
(trainImage, trainLabel), (testImage, testLabel) = mnist.load_data()
print("The data read is complete.")

# 显示前25张图片
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.imshow(testImage[i], cmap='gray')
plt.show()
# 改变维度
testImage = tf.reshape(testImage, (10000, 28, 28, 1))
# 结果预测
result = network.predict(testImage)[0:25]
pred = tf.argmax(result, axis=1)
pred_list = []
for item in pred:
    pred_list.append(item.numpy())
print(pred_list)
