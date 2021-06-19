from artificial_intelligence.final import *

# CNN 网络模型
model = Sequential([
    layers.Conv2D(filters=32, kernel_size=(3, 3), activation=tf.nn.relu,
                  input_shape=(28, 28, 1), padding="same", strides=1),
    layers.BatchNormalization(),
    layers.Conv2D(filters=32, kernel_size=(5, 5), activation=tf.nn.relu, padding="same", strides=1),
    layers.MaxPool2D(pool_size=(2, 2)),
    layers.Dropout(0.5),
    layers.Conv2D(filters=64, kernel_size=(3, 3), activation=tf.nn.relu, padding="same", strides=1),
    layers.BatchNormalization(),
    layers.Conv2D(filters=64, kernel_size=(5, 5), activation=tf.nn.relu, padding="same", strides=1),
    layers.MaxPool2D(pool_size=(2, 2)),
    layers.Dropout(0.5),
    layers.Flatten(),
    layers.Dense(128, activation=tf.nn.relu),
    layers.Dropout(0.5),
    layers.Dense(10, activation=tf.nn.softmax)
])
model.summary()

# 优化器
lr_anneal = callbacks.ReduceLROnPlateau(monitor='val_accuracy', patience=3, factor=0.2, min_lr=1e-6)
rms_prop = optimizers.Adam(learning_rate=1e-3)
# 编译
model.compile(optimizer=rms_prop, metrics=["accuracy"],
              loss=losses.sparse_categorical_crossentropy)
# 模型训练 训练30个epoch
history = model.fit(trainImage, trainLabel, batch_size=100, callbacks=[lr_anneal],
                    epochs=30, validation_data=(testImage, testLabel))

# 模型保存
model.save('./mnist_data/model.h5')
print('The train model saved.')
del model

show(history)
