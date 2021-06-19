import os

from matplotlib import pyplot as plt

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


def show(history):
    fig, ax = plt.subplots(2, 1)
    ax[0].plot(history.history['loss'], color='b', label="Training loss")
    ax[0].plot(history.history['val_loss'], color='r', label="validation loss", axes=ax[0])
    ax[0].legend(loc='best', shadow=True)

    ax[1].plot(history.history['accuracy'], color='b', label="Training accuracy")
    ax[1].plot(history.history['val_accuracy'], color='r', label="Validation accuracy")
    ax[1].legend(loc='best', shadow=True)

    fig.show()
