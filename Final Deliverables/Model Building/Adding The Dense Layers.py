# Adding The Dense Layers


cnn.add(tf.keras.layers.Dense(units=512 ,activation ="relu"))

cnn.add(tf.keras.layers.Dense(units=512 ,activation ="relu"))

cnn.add(tf.keras.layers.Dense(units=9,activation="softmax"))
