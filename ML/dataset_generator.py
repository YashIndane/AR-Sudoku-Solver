import cv2
import csv


# Build the CSV file for training
with open('Digits_Dataset' ,  'w' , newline = '') as f :

 for x in range(0 , 10) :
    for y in range(1 , 161) : 

        address = str(x) + '/' + str(y) + '.png'    

        img = cv2.imread(address)

        rows , cols , _ = img.shape

        data = []
        for i in range(rows) : 
            for j in range(cols) : 
                if img[i][j][0] < 100 : k = 0
                else : k = 1 

                data.append(k)
        
        data.append(x)
        
        writer = csv.writer(f)
        writer.writerow(data)
        
        cv2.waitKey()

f.close()


            




         