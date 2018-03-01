#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:08:17 2018

@author: haichunkan
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 

img_counter = 0
while(True):
    ret,frame = cap.read() # return a single frame in variable `frame`
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('img1',frame)
    #display the captured image
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        s1=cv2.imwrite('image1.jpg',frame)
        cv2.destroyAllWindows()
        break

cap.release()

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 

img_counter = 0
while(True):
    ret,frame = cap.read() # return a single frame in variable `frame`
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('img2',frame)
    #display the captured image
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        s2=cv2.imwrite('image2.jpg',frame)
        gray = cv2.cvtColor(s1, cv2.COLOR_BGR2GRAY)
        cv2.destroyAllWindows()
        break

cap.release()

height = np.size(s1, 0)
width = np.size(s1, 1)
emptyimg = np.zeros((width, height,3),np.uint8)

def pic_sub(dest,s1,s2):
    for x in range(dest.shape[0]):
        for y in range(dest.shape[1]):
            if(s2[x,y] > s1[x,y]):
                dest[x,y] = s2[x,y] - s1[x,y]
            else:
                dest[x,y] = s1[x,y] - s2[x,y]

            if(dest[x,y] < 125):
                dest[x,y] = 0
            else:
                dest[x,y] = 255



pic_sub(emptyimg,s1,s2)

cv2.namedWindow("s1")
cv2.namedWindow("s2")
cv2.namedWindow("result")

cv2.imshow("s1",s1)
cv2.imshow("s2",s2)
cv2.imshow("result",emptyimg)

cv2.waitKey(0)
cv2.destroyAllWindows()