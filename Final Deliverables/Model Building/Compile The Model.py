# Compile the model

  #Optimizer - adam
  #loss function - categorical_crossentropy
  #Metrics used for validating the model - accuracy 


cnn.compile(optimizer="adam",loss="categorical_crossentropy" ,metrics =["accuracy"])


