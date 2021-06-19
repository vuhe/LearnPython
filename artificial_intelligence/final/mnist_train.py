import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 禁用log
import tensorflow as tf
from tensorflow.keras import *

# 加载数据集
mnist = tf.keras.datasets.mnist
(trainImage, trainLabel), (testImage, testLabel) = mnist.load_data()
print("The data read is complete.")

# 数据转换
trainImage = tf.reshape(trainImage, (60000, 28, 28, 1))
testImage = tf.reshape(testImage, (10000, 28, 28, 1))
print("The data conversion is complete.")

# 网络定义
network = Sequential([
    # 卷积层1 (C1)
    layers.Conv2D(filters=6, kernel_size=(5, 5), activation=tf.nn.relu, input_shape=(28, 28, 1), padding="same"),
    # 池化层 (S2)
    layers.MaxPool2D(pool_size=(2, 2), strides=2),
    # 卷积层2 (C3)
    layers.Conv2D(filters=16, kernel_size=(5, 5), activation=tf.nn.relu, padding="same"),
    # 池化层 (S4)
    layers.MaxPool2D(pool_size=2, strides=2),
    # 卷积层3 (C5)
    layers.Conv2D(filters=32, kernel_size=(5, 5), activation=tf.nn.relu, padding="same"),
    # Flatten层 (F6)
    layers.Flatten(),
    # 增加的连接层，用于调整准确率
    layers.Dense(1000, activation=tf.nn.relu),
    layers.Dense(10, activation=tf.nn.softmax)
])
network.summary()

# 编译
network.compile(optimizer='adam', metrics=["accuracy"],
                loss=losses.sparse_categorical_crossentropy)
# 模型训练 训练30个epoch
network.fit(trainImage, trainLabel,
            epochs=30, validation_split=0.1)

# 模型保存
network.save('./mnist_data/model.h5')
print('The train model saved.')
del network
