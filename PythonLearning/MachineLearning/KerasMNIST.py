import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.datasets import mnist

(x_train,y_train), (x_test,y_test) = mnist.load_data()
x_train = x_train.reshape(-1, 28 * 28).astype("float32") / 255.0
x_test = x_test.reshape(-1, 28 * 28).astype("float32") / 255.0
print(x_train.shape)

model =keras.Sequential()
input = keras.Input(shape=28*28)
layer1 = layers.Dense(512,activation='relu')
layer2 = keras.layers.Dense(256,activation='relu')
output=keras.layers.Dense(10,activation='softmax')
model.add(input)
model.add(layer1)
model.add(layer2)
model.add(output)

model.compile(optimizer=keras.optimizers.Adam(lr=0.001),loss=keras.losses.SparseCategoricalCrossentropy(from_logits=False),metrics=['accuracy'])
model.fit(x_train,y_train,batch_size=32,epochs=5,verbose=2)
model.evaluate(x_test,y_test,batch_size=32,verbose=2)