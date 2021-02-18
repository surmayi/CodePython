import tensorflow as tf
from keras.datasets import mnist
from keras import layers
from tensorflow.python.keras import Sequential
from keras import optimizers, losses
from tensorflow.python.keras.utils.np_utils import to_categorical


class MNIST_model:

    # Model initialization
    def __init__(self,input_dim,output_size):
        self.input_dim = input_dim
        self.output_size=output_size

    # CNN layers
    def model_layers(self):
        # 1st CNN layer
        model = Sequential()
        model.add(layers.Conv2D(
            32,
            (5,5),
            activation='relu',
            input_shape=(28,28,1)
        ))
        model.add(layers.MaxPool2D((2,2)))
        model.add(layers.Conv2D(
            64,
            (5,5),
            activation ='relu'
        ))
        model.add(layers.MaxPool2D((2,2)))
        model.add(layers.Flatten())
        model.add(layers.Dense(64,activation='relu'))
        model.add(layers.Dense(10,activation='softmax'))
        model.summary()
        return model

    '''# Add a fully connected layer to the pool2 layer before convertinbg it into logits
    def create_fully_connected_layer(self,pool2):
        # Flattening the pool2 data from NHWC to matrix
        hwc = pool2.shape.as_list()[1:]
        flattened_size= hwc[0]*hwc[1]*hwc[2]
        pool2_flat = tf.reshape(pool2,[-1,flattened_size])

        # Add the fully connected dense layer
        dense = tf.layers.dense(
            pool2_flat,
            1024,       # no. of neurons
            activation=tf.nn.relu,
            name='dense'
        )

        return dense

    # Applying dropouts to avoid co-adaptation
    def apply_dropouts(self,dense,is_training):
        dropout= tf.layers.dropout(
            dense,
            training=is_training,   # Dropouts work only when training the data
            rate=0.4
        )
        return dropout

    def apply_logits(self,dropout):
        logits =tf.layers.dense(
            dropout,
            self.output_size,
            name='logits'
        )
        return logits
'''

    # Classify the output
    def run_model_setup(self,inputs,labels,test_input,test_labels):
        model =self.model_layers()

        model.compile(
        optimizer=optimizers.Adam(lr=0.001),
        loss=losses.categorical_crossentropy,
        metrics=['accuracy']
        )

        model.fit(
        inputs,
        labels,
        batch_size=32,
        epochs=5,
        verbose=1
        )

        model.evaluate(test_input,test_labels,batch_size=32,verbose=1)


    '''    # Find probabilities from logits
        self.probs= tf.nn.softmax(
            logits,
            name='probs'
        )

        # Round to best probability
        self.predictions = tf.argmax(
            self.probs,
            axis=-1,
            name='predictions'
        )

        # Actual labels
        class_labels= tf.argmax(labels,axis=-1)

        # Find correct predictions
        is_correct = tf.equal(
            self.predictions,
            class_labels
        )
        is_correct_float= tf.cast(is_correct, tf.float32)

        # Find accuracy
        self.accuracy = tf.reduce_mean(is_correct_float)
        if self.is_training:
            self.train_model(labels,logits)

    def train_model(self,labels,logits):
        labels_float= tf.cast(labels,tf.float32)

        #Compute the loss function
        cross_entropy = tf.nn.softmax_cross_entropy_with_logits_v2(
            labels=labels_float,
            logits=logits
        )
        self.loss= tf.reduce_mean(cross_entropy)

        # Using Adam optimizer to train the model

        adam = tf.train.AdamOptimizer()
        self.adam_op = adam.minimize(
            self.loss,
            global_step = self.global_step,
            metrics=['accuracy']
        )
'''

(x_train,y_train), (x_test,y_test) = mnist.load_data()
x_train = x_train.reshape(-1, 28 , 28,1).astype("float32") / 255.0
x_test = x_test.reshape(-1, 28 , 28,1).astype("float32") / 255.0
y_test = to_categorical(y_test)
y_train = to_categorical(y_train)
print(x_train.shape)
mnmodel = MNIST_model(28, 10)
print(mnmodel.input_dim,mnmodel.output_size)
mnmodel.run_model_setup(x_train, y_train,x_test,y_test )