import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator


#Data preprocessing
train_datagen = ImageDataGenerator(
                rescale = 1./255,
                shear_range = 0.2,
                zoom_range = 0.2,
                horizontal_flip = True,
                validation_split = 0.05)

training_set = train_datagen.flow_from_directory(
               'PATH',
               target_size = (23,23),
               batch_size =8,
               subset = 'training', 
               class_mode = 'categorical')

#preprocessing dataset
test_datagen = ImageDataGenerator(rescale = 1./255) 
test_set = test_datagen.flow_from_directory(
           'PATH',
           target_size = (23,23),
           batch_size = 8,
           subset = 'validation',
           class_mode = 'categorical' 

)              

#Initialising CNN
cnn = tf.keras.models.Sequential()

#Convolution
cnn.add(tf.keras.layers.Conv2D(filters = 32 , kernel_size = 2 , activation = 'relu' , padding = 'same' , input_shape = [23,23,3]))

#Pooling
cnn.add(tf.keras.layers.MaxPool2D(pool_size = 2 , strides = 2 ,  padding='valid'))

#Adding second convolution layer
cnn.add(tf.keras.layers.Conv2D(filters = 32 , kernel_size = 2 ,padding="same", activation = 'relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size = 2 , strides = 2 ,  padding='valid'))

#Flatening
cnn.add(tf.keras.layers.Flatten())

#full connection
cnn.add(tf.keras.layers.Dense(units = 128 , activation = 'relu'))
cnn.add(tf.keras.layers.Dense(units = 128 , activation = 'relu'))
cnn.add(tf.keras.layers.Dense(units = 128 , activation = 'relu'))
cnn.add(tf.keras.layers.Dense(units = 64 , activation = 'relu'))



#Output layer
cnn.add(tf.keras.layers.Dense(units = 10 , activation = 'softmax'))

#compiling cnn
cnn.compile(optimizer = 'adam' , loss = 'categorical_crossentropy' , metrics = ['accuracy'])

#Training the cnn
cnn.fit(training_set,
                  epochs = 30,
                  steps_per_epoch = 1375,
                  validation_data = test_set,
                  validation_steps = 72)
                  

cnn.save('cnn_110920.h5')

