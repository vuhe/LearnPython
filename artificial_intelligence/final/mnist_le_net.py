from artificial_intelligence.final import *

# LeNet-5 网络模型
model = Sequential([
    layers.Conv2D(filters=6, kernel_size=(5, 5), activation=tf.nn.relu, input_shape=(28, 28, 1), padding="same"),
    layers.MaxPool2D(pool_size=(2, 2), strides=2),
    layers.Conv2D(filters=16, kernel_size=(5, 5), activation=tf.nn.relu, padding="same"),
    layers.MaxPool2D(pool_size=2, strides=2),
    layers.Conv2D(filters=120, kernel_size=(5, 5), activation=tf.nn.relu, padding="same"),
    layers.Flatten(),
    layers.Dense(84, activation=tf.nn.relu),
    layers.Dense(10, activation=tf.nn.softmax)
])
model.summary()

# 编译
model.compile(optimizer=optimizers.Adam(), metrics=["accuracy"],
              loss=losses.sparse_categorical_crossentropy)
# 模型训练 训练5个epoch
history = model.fit(trainImage, trainLabel, epochs=5, validation_data=(testImage, testLabel))

# # 模型保存
# model.save('./mnist_data/model.h5')
# print('The train model saved.')
del model

show(history)
