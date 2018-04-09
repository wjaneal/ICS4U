# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 09:15:37 2018

@author: sg
"""

#Assignment7 OpenCv
#Name:Ketty
#Date: January 25, 2018
'''
Task:
(a) Generate a jpg file with the following:
Rectangles, dots, text, ellipses and lines of different colours.

(b) Take a second .jpg file and edit it to the  same size with a photograph taken by your phone.

(c) Blend the two together in 11 jpg photographs ranging from 0-100%, 10-90%, ... all the way to 100-0%
'''
import numpy as np
import cv2

img1 = np.zeros((600,500,3), np.uint8)#start a new window to set pictures
#Rectangles, dots, text, ellipses and lines of different colours.
cv2.line(img1,(0,50),(199,50),(120,0,0),2)
cv2.line(img1,(40,0),(100,143),(120,115,0),2)
cv2.rectangle(img1,(300,0),(104,150),(0,255,0),3)
cv2.circle(img1,(4,40), 50, (0,0,255), -1)
cv2.circle(img1,(4,40), 0, (225,225,255), 3)
cv2.ellipse(img1,(101,15),(261,30),0,0,180,255,-1)

#write text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img1,'Rem',(100,150), font, 2,(20,100,20),1,cv2.LINE_AA)

img2 = cv2.imread('t11.jpg')  #This is another picture.
#Blend the two pictures ranging from 0-100%, 10-90%, ... all the way to 100-0%.
dst = cv2.addWeighted(img1,0.1,img2,0.9,0)
dst1 = cv2.addWeighted(img1,0.2,img2,0.8,0)
dst2 = cv2.addWeighted(img1,0.3,img2,0.7,0)
dst3 = cv2.addWeighted(img1,0.4,img2,0.6,0)
dst4 = cv2.addWeighted(img1,0.5,img2,0.5,0)
dst5 = cv2.addWeighted(img1,0.6,img2,0.4,0)
dst6 = cv2.addWeighted(img1,0.7,img2,0.3,0)
dst7 = cv2.addWeighted(img1,0.8,img2,0.2,0)
dst8 = cv2.addWeighted(img1,0.9,img2,0.1,0)
dst9 = cv2.addWeighted(img1,1.0,img2,0.0,0)
dst10 = cv2.addWeighted(img1,0.0,img2,1.0,0)
#show
cv2.imshow('dst',dst)
cv2.imshow('dst1',dst1)
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
#save
cv2.imwrite('R.jpg',dst)
cv2.imwrite('R1.jpg',dst1)
cv2.imwrite('R2.jpg',dst2)
cv2.imwrite('R3.jpg',dst3)
cv2.imwrite('R4.jpg',dst4)
cv2.imwrite('R5.jpg',dst5)
cv2.imwrite('R6.jpg',dst6)
cv2.imwrite('R7.jpg',dst7)
cv2.imwrite('R8.jpg',dst8)
cv2.imwrite('R9.jpg',dst9)
cv2.imwrite('R10.jpg',dst10)

cv2.destroyAllWindows()