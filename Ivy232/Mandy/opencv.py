#Assignment7 OpenCv
#Name:Mandy
#Date: January 24, 2018
'''
Task:
(a) Generate a jpg file with the following:
Rectangles, dots, text, ellipses and lines of different colours.

(b) Take a second .jpg file and edit it to the  same size with a photograph taken by your phone.

(c) Blend the two together in 11 jpg photographs ranging from 0-100%, 10-90%, ... all the way to 100-0%
'''
import numpy as np
import cv2
from matplotlib import pyplot as plt
#(a)
img1 = np.zeros((1284,442,3), np.uint8)
cv2.line(img1,(0,183),(235,183),(115,0,0),2)

cv2.rectangle(img1,(10,0),(224,161),(0,255,0),3)
cv2.circle(img1,(4,63), 33, (0,0,255), -1)
cv2.ellipse(img1,(141,15),(161,15),0,0,180,255,-1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img1,'Fly',(30,100), font, 2,(20,100,20),1,cv2.LINE_AA)
'''
cv2.imshow('...',img1)
cv2.waitKey(0)
cv2.imwrite('final.jpg',img1)
cv2.destroyAllWindows()
'''
#(c)

img2 = cv2.imread('AW.jpg')
dst = cv2.addWeighted(img1,0.1,img2,0.9,0)
dst1 = cv2.addWeighted(img1,0.2,img2,0.8,0)
dst2 = cv2.addWeighted(img1,0.3,img2,0.7,0)
dst3 = cv2.addWeighted(img1,0.4,img2,0.6,0)
dst4 = cv2.addWeighted(img1,0.5,img2,0.5,0)
dst5 = cv2.addWeighted(img1,0.6,img2,0.4,0)
dst6 = cv2.addWeighted(img1,0.7,img2,0.3,0)
dst7 = cv2.addWeighted(img1,0.8,img2,0.2,0)
dst8 = cv2.addWeighted(img1,0.9,img2,0.1,0)
dst9 = cv2.addWeighted(img1,1.0,img2,0.0,0)
dst10 = cv2.addWeighted(img1,0.0,img2,1.0,0)

cv2.imshow('dst',dst)
cv2.imshow('dst',dst1)
cv2.imshow('dst',dst2)
cv2.imshow('dst',dst3)
cv2.imshow('dst',dst4)
cv2.imshow('dst',dst5)
cv2.imshow('dst',dst6)
cv2.imshow('dst',dst7)
cv2.imshow('dst',dst8)
cv2.imshow('dst',dst9)
cv2.imshow('dst',dst10)

cv2.waitKey(0)

cv2.imwrite('final.jpg',dst)
cv2.imwrite('final1.jpg',dst1)
cv2.imwrite('final2.jpg',dst2)
cv2.imwrite('final3.jpg',dst3)
cv2.imwrite('final4.jpg',dst4)
cv2.imwrite('final5.jpg',dst5)
cv2.imwrite('final6.jpg',dst6)
cv2.imwrite('final7.jpg',dst7)
cv2.imwrite('final8.jpg',dst8)
cv2.imwrite('final9.jpg',dst9)
cv2.imwrite('final10.jpg',dst10)

cv2.destroyAllWindows()


