# -*- coding: utf-8 -*-
'''

(b) Name:Emma,
Date: Created on Wed Jan 24 12:49:41 2018, 
Title:#Assignment 7 - OpenCV, 
Purpose:
(a)To generate a jpg file with Rectangles, dots, text, 
ellipses and lines of different colours.

(b) Take a second .jpg file and edit it to the  same size with a photograph 
taken by your phone.

(c) Blend the two together in 11 jpg photographs ranging from 0-100%, 
10-90%, ... all the way to 100-0%

'''
#Import sources required
import numpy as np
import cv2
from matplotlib import pyplot as plt 

#(a)

# Create a black image
img1 = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
img1 = cv2.line(img1,(399,5),(5,399),(226,0,0),5)
# Draw a green rectangle at the top-right corner of image
img1 = cv2.rectangle(img1,(20,384),(510,128),(0,255,0),3)
# Draw a half ellipse at the center of the image.
img1 = cv2.ellipse(img1,(256,256),(100,50),0,0,360,(89,42,256),-1)
#Draw a dot including its center coordinates, radius, and color.
img1 = cv2.circle(img1,(-1,30),10,(255,127,80),-1)
# Write "Emma" on our image in white color.
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img1,'Emma',(10,500), font, 5,(255,255,255),2,cv2.LINE_AA)
#Display the image
cv2.imshow('image1',img1)
k = cv2.waitKey(0)
if k == 27:# wait for ESC key to exit
    cv2.destroyAllWindows()

#(b)
#load a image with same size
img2 = np.zeros((512,512,3), np.uint8)
# Draw a  rectangle at the top-right corner of image
img2 = cv2.rectangle(img2,(255,-4),(450,268),(5,140,243),15)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img2,'Eddie',(10,300), font, 6,(219,112,255),2,cv2.LINE_AA)
#Draw a circle including its center coordinates, radius, color, and thickness.
img2 = cv2.circle(img2,(255,256),159,(159,112,80),20)
cv2.namedWindow('image2', cv2.WINDOW_NORMAL)
#Display the image
cv2.imshow('image2',img2)
k = cv2.waitKey(0)
if k == 27:# wait for ESC key to exit
    cv2.destroyAllWindows()

#(c)
for i in range(0,11):#Blend them in 11 different photographs by setting a for loop
    dst = cv2.addWeighted(img1,1-i/10,img2,i/10,0)
    cv2.imshow('imagesblended',dst)
    k = cv2.waitKey(0)
    if k == 27:# wait for ESC key to exit
        cv2.destroyAllWindows()
