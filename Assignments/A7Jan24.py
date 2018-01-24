

'''#Assignment 7 - OpenCV

Coding convention: 
(a) lower case file name
(b) Name, Date, Title, Purpose in multiline comment at the beginning
(c) mixedCase variable names

Task:
(a) Generate a jpg file with the following:
Rectangles, dots, text, ellipses and lines of different colours.

(b) Take a second .jpg file and edit it to the  same size with a photograph taken by your phone.

(c) Blend the two together in 11 jpg photographs ranging from 0-100%, 10-90%, ... all the way to 100-0%

'''
import numpy as np
import cv2
img = np.zeros((512,512,3), np.uint8) #This line is to create a black image
cv2.line(img,(0,0),(511,511),(255,0,0),5)#This
#This line is to show the image
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
