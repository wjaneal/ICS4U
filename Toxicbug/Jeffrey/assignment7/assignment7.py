 # -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 13:03:22 2018

@author: Jeffrey

Purpose:
(a) Generate a jpg file with the following:
Rectangles, dots, text, ellipses and lines of different colours.

(b) Take a second .jpg file and edit it to the  same size with a photograph taken by your phone.

(c) Blend the two together in 11 jpg photographs ranging from 0-100%, 10-90%, ... all the way to 100-0%
"""

import numpy as np
import cv2

img1 = cv2.imread('husky.jpeg')
img2 = cv2.imread('boat.jpg')


# Draw a diagonal blue line with thickness of 5 px
cv2.line(img1,(0,0),(1000,800),(100,0,255),3)
# Draw a rectangle
cv2.rectangle(img1,(384,0),(510,128),(0,255,0),3)
# Draw a Circle
cv2.circle(img1,(447,600), 100, (0,0,255), -1)
# Draw a ellipse
cv2.ellipse(img1,(256,256),(100,50),200,0,255,255,-1)
# Draw a dot
cv2.circle(img1,(120,300), 4, (100,0,255), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img1,'Husky',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)


cv2.imshow('husky.jpeg',img1)

cv2.imshow('boat.jpg',img2)


img1 = cv2.imread('husky.jpeg')
img2 = cv2.imread('boat.jpg')
dst = ['1','2','3','4','5','6','7','8','9','10']
for i in range(10):
    dst[i] = cv2.addWeighted(img1,i/10,img2,1-i/10,0)
    cv2.imshow(str(dst[i]),dst[i])
cv2.waitKey(0)
cv2.destroyAllWindows()