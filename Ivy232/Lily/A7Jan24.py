# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

 #import module

img = np.zeros((621,827,3), np.uint8) #set up a canvass
cv2.rectangle(img,(500,0),(200,400),(0,255,0),3) #draw a rectangle start from (500,0) to (200,789)
cv2.ellipse(img,(589,220),(200,200),0,0,-180,(255,211,89),-1) #draw a ellipse
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX  #set font
cv2.putText(img,'Hello Sky',(10,500), font, 4,(100,234,200),2,cv2.LINE_AA) #write text
cv2.circle(img,(230,230), 23, (233,125,135), -1)#draw circle with radius of 23 starting from (230,230)
cv2.circle(img,(460,230), 23, (233,125,135), -1)
cv2.circle(img,(690,230), 23, (233,125,135), -1)
cv2.line(img,(103,299),(551,299),(255,0,0),2) #draw a line start from (103,229) to (551,229), the width of line is "2"
cv2.line(img,(103,103),(448,103),(123,69,0),2)
cv2.line(img,(103,206),(345,206),(78,178,178),2)
cv2.imwrite('self.jpg',img)


#Save as a .jpg file
#img = cv2.imread('hahahahage.jpg', 0)
img1 = cv2.imread('hahahahage1.jpg') #imput the picture I originally have
img2 = cv2.imread('self.jpg') #imput the picture I drew in the first part
i = 0
for i in range(0,11):
    dst = cv2.addWeighted(img2,i/10,img1,(1-i/10),0)
    cv2.imwrite('copy'+str(i)+'.jpg',dst)
    
    cv2.imshow('dst',dst) #print the images
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    



    








