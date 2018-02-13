# -*- coding: utf-8 -*-
"""
Name: Xu, Yingjie (Mike)
Date: 2018-01-24
Program Title: assignment7 (opencv)
Purpose: 
(a) Generate a jpg file with the following: Rectangles, dots, text, ellipses and lines of different colours.
(b) Take a second .jpg file and edit it to the  same size with a photograph taken by your phone.
(c) Blend the two together in 11 jpg photographs ranging from 0-100%, 10-90%, ... all the way to 100-0%
"""
import numpy as np
import cv2

cv2.imwrite('2.jpg',img) #This could create a picture
img = np.zeros((512,512,3), np.uint8) #This could define the dimention of the picture
cv2.line(img,(0,0),(511,511),(255,0,255),5) #This could draw a line
cv2.rectangle(img,(384,0),(250,250),(0,255,0),3) #This could draw rectangle
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1) #This could draw ellipses
cv2.circle(img,(450,250), 5, (0,0,255), -1) #This could draw a dot
cv2.line(img,(511,0),(0,511),(255,255,0),5) #This could draw a line of diffenert color
font = cv2.FONT_HERSHEY_SIMPLEX #This could write some texts
cv2.putText(img,'Computer Science',(10,500), font, 1,(255,255,255),2,cv2.LINE_AA)

img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')
for i in range(0,11): #This loop could blend two pictures together for 11 times.
    dst = cv2.addWeighted(img1,i/10,img2,(1-i/10),0) #This could change the weight of two different images.
    cv2.imwrite('picture'+str(i+1)+'.jpg',dst)
