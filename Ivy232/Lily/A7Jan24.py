# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt #import module
img = np.zeros((621,827,3), np.uint8) #set up a canvass
cv2.rectangle(img,(500,0),(200,789),(0,255,0),3) #draw a rectangle start from (500,0) to (200,789)
cv2.ellipse(img,(589,220),(200,200),0,0,-180,(255,211,89),-1) #draw a ellipse
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX  #set font
cv2.putText(img,'Hello Sky',(10,500), font, 4,(100,234,200),2,cv2.LINE_AA) #write text
cv2.circle(img,(230,230), 23, (233,125,135), -1)#draw circle with radius of 23 starting from (230,230)
cv2.circle(img,(460,230), 23, (233,125,135), -1)
cv2.circle(img,(690,230), 23, (233,125,135), -1)
cv2.line(img,(103,299),(551,299),(255,0,0),2) #draw a line start from (103,229) to (551,229), the width of line is "2"
cv2.line(img,(103,103),(448,103),(123,69,0),2)
cv2.line(img,(103,206),(345,206),(78,178,178),2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindow()

#Save as a .jpg file
#img = cv2.imread('hahahahage.jpg', 0)
img1 = cv2.imread('hahahahage.jpg') #imput the picture I originally have

dst1 = cv2.addWeighted(img1,1,img,0,0) #merge the two pictures together
dst2 = cv2.addWeighted(img1,0.9,img,0.1,0)
dst3 = cv2.addWeighted(img1,0.8,img,0.2,0)
dst4 = cv2.addWeighted(img1,0.7,img,0.3,0)
dst5 = cv2.addWeighted(img1,0.6,img,0.4,0)
dst6 = cv2.addWeighted(img1,0.5,img,0.5,0)
dst7 = cv2.addWeighted(img1,0.4,img,0.6,0)
dst8 = cv2.addWeighted(img1,0.3,img,0.7,0)
dst9 = cv2.addWeighted(img1,0.2,img,0.8,0)
dst10 = cv2.addWeighted(img1,0.1,img,0.9,0)
cv2.imshow('dst1',dst1) #print the images
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)
cv2.imshow('dst4',dst4)
cv2.imshow('dst5',dst5)
cv2.imshow('dst6',dst6)
cv2.imshow('dst7',dst7)
cv2.imshow('dst8',dst8)
cv2.imshow('dst9',dst9)
cv2.imshow('dst10',dst10)
cv2.waitKey(0)

cv2.imwrite('image1', dst1) #store the images
cv2.imwrite('image2', dst2)
cv2.imwrite('image3', dst3)
cv2.imwrite('image4', dst4)
cv2.imwrite('image5', dst5)
cv2.imwrite('image6', dst6)
cv2.imwrite('image7', dst7)
cv2.imwrite('image8', dst8)
cv2.imwrite('image9', dst9)
cv2.imwrite('image10', dst10)
cv2.destroyAllWindows()


