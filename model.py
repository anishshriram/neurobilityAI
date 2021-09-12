import tensorflow as tf
import numpy as np

path = '/Users/anishshriram/Downloads/mnist.npz'

# Callback class which has a function that stops epochs after 99% accuracy
class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if logs.get('accuracy') > 0.99:
            self.model.stop_training = True


# Loading the MNIST dataset
mnist = tf.keras.datasets.mnist

# Giving two sets of lists, for training and testing values for the graphics that contain the digits and labels
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data(path=path)

# Normalizing (instead of the numbers being from 0 -> 255, make it from 0-1)
# In python, you don't have to loop through the list - just divide entire thing
x_train, x_test = x_train / 255.0, x_test / 255.0

# Instantiate the above class
callbacks = myCallback()

'''
For the model:
Sequential: Defines the SEQUENCE of layers in the neural network
Flatten: Images are a square, flatten takes the square and turns it into a one dimensional set
Dense: Adds a layer of neurons
    Needs activation functions to tell them what to do
    Relu: Basically, if X > 0 return X, else return 0
    Softmax: Takes a set of values, and picks out the biggest one
'''
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

# Now actually build the model. Compiling with the optimizer and loss function as before
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the neural network by calling model.fit()
# Will stop training after reaching 99% accuracy
model.fit(x_train, y_train, epochs=10, callbacks=[callbacks])
'''
test = x_test[0].reshape(-1,28,28)
test /=255.0
pred = model.predict(test)
predict = np.argmax(pred)
print(predict)
'''

# Saving the model as an h5 file
model.save('model.h5')
