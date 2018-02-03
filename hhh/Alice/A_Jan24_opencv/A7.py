#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 13:15:32 2018
Program:OpenCV
Purpose:
(a) Generate a jpg file with the following:
Rectangles, dots, text, ellipses and lines of different colours.
(b) Take a second .jpg file and edit it to the  same size with a photograph taken by your phone.
(c) Blend the two together in 11 jpg photographs ranging from 0-100%, 10-90%, ... all the way to 100-0%
@author: haichunkan
"""

import cv2
import numpy as np
img = cv2.imread('mypicture.jpg',1)#Edit the first picture.
img = cv2.line(img,(297,399),(720,74),(255,0,0),5)#Draw a line.
img = cv2.rectangle(img,(726,0),(831,72828),(0,255,0),3)#Draw a rectangle.
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)#Draw a circle.
img = cv2.ellipse(img,(325,600),(100,50),0,0,180,255,-1)#Draw an ellipse.
font = cv2.FONT_HERSHEY_SIMPLEX#Add words.
cv2.putText(img,'Alice in Wonderland',(10,500), font, 2,(255,255,255),2,cv2.LINE_AA)

img2 =cv2.imread('150.jpg',1)#This is the second picture.
for i in range(0,11):
    new=cv2.addWeighted(img,i/10.0,img2,(10-i)/10.0,0)#Blend them together.
    cv2.imshow('new',new)#Show the picture.
    w=cv2.waitKey(0)#change image.
    cv2.destroyAllWindows()
