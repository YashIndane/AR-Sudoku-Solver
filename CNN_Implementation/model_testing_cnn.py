import keras
from itertools import compress
from keras.preprocessing import image
import numpy as np

# This code returns the predicted grid as a list using Convolutional Neural Networks
def generate_grid() -> list : 
    
    digits = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
    model = keras.models.load_model('cnn_110920.h5')

    sudoku_array , temp , emp_arr = [] , [] , []
    # emp_arr contains the indexes where the cell is empty

    for p in range(1 , 82) :
        
        img_addr = f'sample{p}.png'
        input_image = image.load_img(img_addr , target_size = (23 ,23))
        input_image = image.img_to_array(input_image)
        input_image = np.expand_dims(input_image , axis = 0)
        result = model.predict(input_image)

        len_pre = len(''.join([str(x) for x in result[0]]))
        NUM = 0 if len_pre > 30 else list(compress(digits , result[0]))[0]

        temp.append(NUM) 

        if NUM == 0 : emp_arr.append(p - 1)
    
        if p % 9 == 0 : 
             sudoku_array.append(temp)
             temp = []
         
    return [sudoku_array , emp_arr]
