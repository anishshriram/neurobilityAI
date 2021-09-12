import tensorflow as tf
import numpy as np

path = '/Users/anishshriram/Downloads/mnist.npz'


class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if logs.get('accuracy') > 0.99:
            self.model.stop_training = True


mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data(path=path)
x_train, x_test = x_train / 255.0, x_test / 255.0

callbacks = myCallback()

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10, callbacks=[callbacks])
'''
test = x_test[0].reshape(-1,28,28)
test /=255.0
pred = model.predict(test)
predict = np.argmax(pred)
print(predict)
'''

model.save('model.h5')
