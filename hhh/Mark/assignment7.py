# -*- coding: utf-8 -*-
"""
Name: Song, Jiwei (Mark)
Date: 2018-01-24
Program Title: OpenCV
Purpose:
(a) Generate a jpg file with the following:
Rectangles, dots, text, ellipses and lines of different colours.
(b) Take a second .jpg file and edit it to the  same size with a photograph taken by your phone.
(c) Blend the two together in 11 jpg photographs ranging from 0-100%, 10-90%, ... all the way to 100-0%
"""

import cv2
import numpy as np
img1 = cv2.imread('3.jpeg')
img2 = cv2.imread('2.jpg')

img = np.zeros((512,512,3), np.uint8)
cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
cv2.circle(img,(150,300), 4, (100,0,255), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Hello, CS',(10,500), font, 2,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('3.jpeg',img1)

cv2.imshow('2.jpg',img2)

img1 = cv2.imread('3.jpeg')
img2 = cv2.imread('2.jpg')
dst = ['1','2','3','4','5','6','7','8','9','10']
for i in range(10):
    dst[i] = cv2.addWeighted(img1,i/10,img2,1-i/10,0)
    cv2.imshow(str(dst[i]),dst[i])
cv2.waitKey(0)
cv2.destroyAllWindows()