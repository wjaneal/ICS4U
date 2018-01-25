#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 12:57:17 2018
@author: hailankan
title: opencv practice
purpose:
(a) Generate a jpg file with the following:
Rectangles, dots, text, ellipses and lines of different colours.
(b) Take a second .jpg file and edit it to the  same size with a photograph taken by your phone.
(c) Blend the two together in 11 jpg photographs ranging from 0-100%, 10-90%, ... all the way to 100-0%
"""

import numpy as np
import cv2


img=cv2.imread('hmbb.jpg',1)
cv2.circle(img,(200,200),10,(255,255,0),-1)
cv2.line(img, (100,100), (300,300), (0,0,255),4)
cv2.rectangle(img, (230,120), (400,270), (0,255,0), 5)
cv2.ellipse(img, (300, 200), (100, 50), 20, 30, 70, (255,0,0), 6)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Hello everybody!', (230, 50), font, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
cv2.imshow('image',img)

img2 = cv2.imread('xg.jpg')
for i in range(0,11):
    new = cv2.addWeighted(img2,i/10,img,1.0-i/10,0)
    cv2.imshow('blending'+str(i+1),new)


cv2.waitKey(0)
cv2.destroyAllWindows()

