training_set = train_datagen.flow_from_directory(
        'Train_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical',
        color_mode = "grayscale")


test_data = test_datagen.flow_from_directory(
        'Test_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical',
        color_mode = "grayscale")
