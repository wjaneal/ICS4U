

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
from matplotlib import pyplot as plt
img = np.zeros((1000,1000,3), np.uint8)
cv2.rectangle(img,(300,100),(200,289),(0,255,0),3)
cv2.ellipse(img,(589,580),(100,50),0,0,180,255,-1)
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(img,'Hello Sky',(10,500), font, 4,(200,100,2),2,cv2.LINE_AA)
cv2.circle(img,(230,230), 23, (0,125,255), -1)
cv2.circle(img,(460,230), 23, (0,125,255), -1)
cv2.circle(img,(690,230), 23, (0,125,255), -1)
cv2.line(img,(0,0),(551,228),(255,0,0),5)
cv2.line(img,(0,0),(448,125),(123,69,0),5)
cv2.line(img,(0,0),(345,22),(255,0,178),5)



#Save as a .jpg file
img = cv2.imread('hahahahage.jpg',0)
img1 = cv2.imread('hahahahage1.jpg',0)
dst1 = cv2.addWeighted(img1,1.0,img,0.0,0)
dst2 = cv2.addWeighted(img1,0.9,img,0.1,0)
dst3 = cv2.addWeighted(img1,0.8,img,0.2,0)
dst4 = cv2.addWeighted(img1,0.7,img,0.3,0)
dst5 = cv2.addWeighted(img1,0.6,img,0.4,0)
dst6 = cv2.addWeighted(img1,0.5,img,0.5,0)
cv2.imshow('dst3',dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()
