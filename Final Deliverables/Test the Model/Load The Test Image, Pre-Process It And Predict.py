
# Preprocessing the image to be tested
img_rgb = cv2.imread('prediction/F.jpg')

# converting the rgb image into grayscale 
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) 


 # saving it as new img in the specified location
cv2.imwrite("prediction/result.jpg",img_gray)  


#Loading the test image 
image = tf.keras.preprocessing.image.load_img("prediction/result.jpg",color_mode="grayscale",target_size=(64,64))

# converting the image to array 
input_arr = tf.keras.preprocessing.image.img_to_array(image)


input_arr = np.expand_dims(input_arr,axis=0)

#predicting the image to be tested 
result = cnn.predict(input_arr)

O/P  1/1 [==============================] - 0s 19ms/step

training_set.class_indices

O/P  {'B': 0, 'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5, 'H': 6, 'I': 7}

print(result)

[[0. 0. 0. 0. 1. 0. 0. 0.]]
