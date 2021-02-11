import cv2
import numpy as np

#Fill the screen with digits
def fill_digits_motion(num_array , coor_array , indexes , tos):
  
   cap=cv2.VideoCapture(0)

   
   if cap.isOpened() : ret,frame = cap.read()

   else:
      ret = False

   ret,frame1 = cap.read()
   ret,frame2 = cap.read()

  
   diff = 0
   
   while ret:
      
      ret,frame = cap.read()
      
      d=cv2.absdiff(frame1,frame2)

      grey=cv2.cvtColor(d,cv2.COLOR_BGR2GRAY)

      blur =cv2.GaussianBlur(grey,(5,5),0)
      ret,th=cv2.threshold(blur,40,255,cv2.THRESH_BINARY)
      dilated=cv2.dilate(th,np.ones((3,3),np.uint8),iterations = 3)
      c,h=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
      
      for cnt in c :
          area = cv2.contourArea(cnt)

          if area > 27000 : #This value can be adjusted

               approx = cv2.approxPolyDP(cnt,   0.1 * cv2.arcLength(cnt, True), True) 

               if len(approx) == 4 : 
                  
                  x , y , w , h = cv2.boundingRect(cnt) 
                  diff = x - coor_array[0][0]  
                  
                  
      font = cv2.FONT_HERSHEY_SIMPLEX

      frame1 = cv2.putText(frame1 , tos , (15 , 35) , font , 0.5 , (255 , 255 , 0) , 1 , cv2.LINE_AA)

          
      for i in indexes : 
              
        digit = str(num_array[i])
        position = coor_array[i]
        
        frame1 = cv2.putText(frame1 , digit , (position[0] + diff + 18 , position[1] + 10) , font , 0.5 , (255 , 0 , 255) , 1 ,cv2.LINE_AA) 

      
      cv2.imshow("Sudoku Solved",frame1)
      
      if cv2.waitKey(40) == 27:
         break
      frame1 = frame2
      ret,frame2= cap.read()

   cv2.destroyAllWindows()