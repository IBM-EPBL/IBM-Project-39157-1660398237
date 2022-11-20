#Fitting(Training) the model

cnn.fit(training_set , validation_data =test_data , epochs = 40 )

# Saving the model

cnn.save("aslpng.h5")
