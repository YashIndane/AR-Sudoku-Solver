import cv2
import numpy as np

# This code captures all the square grids on the board and saves it
def capture_save() -> list : 
    
    cap = cv2.VideoCapture(0)
   
    flag = True
    c , m = 0 , 0
    cnt_array = []


    while flag:


        success, img_org = cap.read()
    
        img = cv2.cvtColor(img_org , cv2.COLOR_BGR2GRAY)
    
        _ , threshold = cv2.threshold(img, 110 , 255 ,cv2.THRESH_BINARY) 

        contours , _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    
        if len(contours) > 350 : 
          for cnt in contours : 
        
            area = cv2.contourArea(cnt) 
    
            # Capturing grid squares by area 
            if area > 350 :  
                approx = cv2.approxPolyDP(cnt,   0.03 * cv2.arcLength(cnt, True), True) 
    
                # Only grabbing 4 sided polygons
                if(len(approx) == 4):  
                   

                    x , y , w , h = cv2.boundingRect(cnt)  
                    
                    if all([w > 20 , w < 48 , h > 20 , h < 48]) : 
                        cv2.drawContours(img_org, [approx], 0, (0, 0, 255), 2) 
                        if [x , y] not in cnt_array : 
                             cnt_array.append([x , y])
                             c += 1
                        

                        if c == 81 :  
                            flag = False
                            break

        if c == 81 :  
            flag = False                    
                            
            cnt_array = sorted(cnt_array , key = lambda x : x[1])
            fin_cnt_array = []
        
            a , b = 0 , 9
            for i in range(9) : 
                temp = cnt_array[a : b]
                first_y = temp[0][1]
                for elements in temp : elements[1] = first_y + 2
                a += 9
                b = a + 9
                fin_cnt_array.append(temp)
        
            temp_chunk = []
            for chunk in fin_cnt_array : 
                temp_c = sorted(chunk , key = lambda v : v[0])
                for c in temp_c : temp_chunk.append(c)

            fin_cnt_array = temp_chunk
              

            k = 0 
            for images in fin_cnt_array : 
                k += 1
                x , y = images
                image = img[y : y + 23 , x : x + 23]
                s = 'sample' + str(k) + '.png'
                cv2.imwrite(s , image)

        cv2.imshow("Grid Detection", img_org)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    return fin_cnt_array    