cnn.add(tf.keras.layers.Conv2D(filters=64,kernel_size=3,activation ="relu",input_shape =[64,64,1]))

cnn.add(tf.keras.layers.MaxPool2D(pool_size = 2,strides=2))

cnn.add(tf.keras.layers.Conv2D(filters=64,kernel_size=3,activation ="relu"))

cnn.add(tf.keras.layers.MaxPool2D(pool_size = 2,strides=2))

cnn.add(tf.keras.layers.Conv2D(filters=64,kernel_size=3,activation ="relu"))

cnn.add(tf.keras.layers.MaxPool2D(pool_size = 2,strides=2))
