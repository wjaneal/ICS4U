# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:48:25 2018

@author: Chris-Li
"""

import cv2
import numpy as np

# Load an color image in grayscale
img1 = cv2.imread('mario.jpg'，0)
img2 = cv2.imread("path.jpg",1)

# Draw a line
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
cv2.putText(img1,'mario',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

img2 =cv2.imread('path.jpg',1)#This is the second picture.
dst = ['1','2','3','4','5','6','7','8','9','10']
for i in range(0,10):
    dst[i] = cv2.addWeighted(img1,i/10,img2,1-i/10,0)
    cv2.imshow(str(dst[i]),dst[i])
cv2.waitKey(0)#change image.
cv2.destroyAllWindows()
