#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name:chenquancheng
Date:Created on Tue Jan 23 13:00:34 2018
Title: image operations
Purpose:This program generates some .jpg files and creates some drawings on it. It also merges two .jpg files.
"""
#This part generates a jpg file and creates some drawings.
import cv2
import numpy as np
img = cv2.imread('img2.jpg')
#This creates a line.
cv2.line(img,(0,0),(511,511),(0,255,255),5)
#This creates a rectangle.
cv2.rectangle(img,(100,0),(200,100),(0,255,0),3)
#This creates an ellipse.
cv2.ellipse(img,(66,246),(100,50),100,0,360,255,-1)
#This creates some texts.
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'ICS4U',(300,178), font, 1,(255,255,255),2,cv2.LINE_AA)
#This creates a dot.
cv2.circle(img,(150,50), 9, (0,0,255), -1)
#This shows the image.
cv2.imshow('image',img)
#This saves the image as a .png file.
cv2.imwrite('img2.png',img)
#This part merges two images.
img1 = cv2.imread('img1.jpg')
img2 = cv2.imread('img2.png')
#This loop creates 11 .jpg photographs.
new=[]
for i in range(0,11):
    dst = cv2.addWeighted(img1,i/10,img2,(1-i/10),0)
    cv2.imwrite('blending'+str(i+1)+'.jpg',dst)
#This closes the image.
cv2.waitKey(0)
cv2.destroyAllWindows()
    

