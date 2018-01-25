# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 12:47:05 2018
Name: Jaune
Date: Jan 24
Title: openCV
Purpose: editing pictures
@author: CTL
"""

import numpy as np
import cv2
img = np.zeros((1000,1777,3), np.uint8) #This line is to create a black image
cv2.line(img,(0,0),(511,511),(255,0,0),5)#This is to drwa a blue line
cv2.rectangle(img,(900,0),(343,656),(0,255,0),3)#This line is to draw a rectangle
cv2.circle(img,(447,63), 63, (0,0,255), -1)#This line is to draw a circle
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)#This line is to draw a ellipse
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'shutDown',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)#This line is to put a text

#This line is to show the image
cv2.imshow('image',image)

''''
#This line is to save the image
cv2.inwrite('black.png',img)
''''

img1 = cv2.imread('black.png')
img2 = cv2.imread('glassess.png')

#This is to blend two pictures
dst = cv2.addWeighted(img1,0.0,img2,1.0,0)
dst = cv2.addWeighted(img1,0.1,img2,0.9,0)
dst = cv2.addWeighted(img1,0.2,img2,0.8,0)
dst = cv2.addWeighted(img1,0.3,img2,0.7,0)
dst = cv2.addWeighted(img1,0.4,img2,0.6,0)
dst = cv2.addWeighted(img1,0.5,img2,0.5,0)
dst = cv2.addWeighted(img1,0.6,img2,0.4,0)
dst = cv2.addWeighted(img1,0.7,img2,0.3,0)
dst = cv2.addWeighted(img1,0.8,img2,0.2,0)
dst = cv2.addWeighted(img1,0.9,img2,0.1,0)
dst = cv2.addWeighted(img1,1.0,img2,0.0,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()





















