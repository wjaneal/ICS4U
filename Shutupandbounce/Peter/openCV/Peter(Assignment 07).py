#Name:Peter Zeng

#Date: January 24, 2018

#Program Title: OpenCV

#Program Function:a) Generate a jpg file with the following:
#Rectangles, dots, text, ellipses and lines of different colours.

#(b) Take a second .jpg file and edit it to the  same size with a photograph taken by your phone.

#(c) Blend the two together in 11 jpg photographs ranging from 0-100%, 10-90%, ... all the way to 100-0%

import cv2
import numpy as np

#a
img = np.zeros((400,400,3),np.uint8)
img = cv2.imread('001.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(15,25),(350,250),(255,255,255),15)
cv2.rectangle(img,(15,25),(300,150),(0,255,255),5)
cv2.circle(img,(150,234),55,(0,0,255),-1)
cv2.ellipse(img,(250,300),(105,100),0,0,360,(53,150,300),-2)

pts = np.array([[10,5],[15,20],[30,25],[90,30]],np.int32)
cv2.polylines(img,[pts],True,(255,255,0),2)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Peter Parker!!!',(0,200),font,1,(200,255,255),2,cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#b
img1 = np.zeros((400,400,3),np.uint8)
img1 = cv2.imread('002.jpg',cv2.IMREAD_COLOR)

cv2.ellipse(img1,(250,300),(105,100),0,0,360,(53,150,300),-2)
cv2.line(img1,(0,0),(150,250),(255,255,255),10)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img1,'Success!!',(0,200),font,1,(200,255,255),2,cv2.LINE_AA)

cv2.imshow('image1',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#c
for p in range(0,11):
    dst = cv2.addWeighted(img,1-p/10,img1,p/10,0)
    cv2.imshow('photoscombination',dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()





