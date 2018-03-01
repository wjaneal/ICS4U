# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 02:39:57 2018

@author: 11256
"""
''' 
(a)Name:Tony
(b)Date:January 25th
(c)Program title: opencv
(d)Purpose:Generate a jpg file with the following:Rectangles, dots, text, ellipses and lines of different colours
   Blend the two together in 11 jpg photographs ranging from 0-100%, 10-90%, ... all the way to 100-0%
'''
import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(0,0),(511,511),(255,0,0),5)
#creat a rectangle
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
#creat a circle
cv.circle(img,(447,63), 63, (0,0,255), -1)
#creat a dot
cv.circle(img,(200,63), 10, (0,0,255), -1)
#creat a ellipse
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
#creat the text
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)


cv.imwrite('black.jpg',img)


img1 = cv.imread('black.jpg')
img2 = cv.imread('is.jpg')
dst = cv.addWeighted(img1,0.0,img2,1.0,0)
#blend the two picture together
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()
dst = cv.addWeighted(img1,0.1,img2,0.9,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()
dst = cv.addWeighted(img1,0.2,img2,0.8,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()
dst = cv.addWeighted(img1,0.3,img2,0.7,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()
dst = cv.addWeighted(img1,0.4,img2,0.6,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()
dst = cv.addWeighted(img1,0.5,img2,0.5,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()
dst = cv.addWeighted(img1,0.6,img2,0.4,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()
dst = cv.addWeighted(img1,0.7,img2,0.3,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()
dst = cv.addWeighted(img1,0.8,img2,0.2,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()
dst = cv.addWeighted(img1,0.9,img2,0.1,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()
dst = cv.addWeighted(img1,1.0,img2,0.0,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()