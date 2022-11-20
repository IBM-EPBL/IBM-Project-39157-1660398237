

def hello_world():
    if(request.method=='POST'):
        model = load_model('aslpng.h5')

        # CAMERA can be 0 or 1 based on default camera of your computer.
        camera = cv2.VideoCapture(0)

        # Grab the labels from the labels.txt file. 
        labels = open('labels.txt', 'r').readlines()

        while True:

            # Grab the webcameras image.
            ret, image = camera.read()

            # Resize the raw image into (224-height,224-width) pixels.
            image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

            # Show the image in a window
            orig_img = image
            
            
            # Convert the image into a numpy array and reshape it to the models input shape.
            image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

            # Normalize the image array
            image = (image / 127.5) - 1

        

            #Predict the image using the model 
            probabilities = model.predict(image)
           
            # Print what the highest value probabilities label
            print(labels[np.argmax(probabilities)])
            
            
            
            font                   = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (30,50)
            fontScale              = 1
            fontColor              = (255,0,0)
            thickness              = 3
            lineType               = 2
            
            cv2.putText(orig_img,labels[np.argmax(probabilities)], 
            bottomLeftCornerOfText, 
            font, 
            fontScale,
            fontColor,lineType)
            
            
            cv2.imshow('Webcam Image', orig_img)
            
            
            
            # Listen to the keyboard for presses.
            keyboard_input = cv2.waitKey(1)
            # 27 is the ASCII for the esc key on your keyboard.
            if keyboard_input == 27:
                break

        camera.release()
        cv2.destroyAllWindows()
        return("Thankyou....")
    else:
	    return render_template('index.html')

# main driver function
if __name__ == '__main__':

	app.run(debug=True)
