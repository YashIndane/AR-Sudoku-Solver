import joblib
import cv2

# This code returns the predicted grid as a list using random forest classification
def generate_grid() -> list : 
    
    model = joblib.load('RFC_160')
    sudoku_array = []
    temp = []
    emp_arr = [] # This array contains the indexes where there is no value

    for p in range(1 , 82) :

        adress_text = 'sample' + str(p) + '.png'
        img = cv2.imread(adress_text)
        rows , cols , _ = img.shape
        data_image = []

        for i in range(rows) : 
            for j in range(cols) : 
                  if img[i][j][0] < 100 : k = 0
                  else : k = 1

                  data_image.append(k)
        
        NUM = model.predict([data_image])[0]
        temp.append(NUM) 

        if NUM == 0 : emp_arr.append(p - 1)
    
        if p % 9 == 0 : 
             sudoku_array.append(temp)
             temp = []
         
    return [sudoku_array , emp_arr]

   




    


  