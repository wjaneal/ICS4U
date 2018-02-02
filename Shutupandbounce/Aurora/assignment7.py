'''#Assignment 7 - OpenCV
#Name:Aurora Hou
#Date:Jan,25,2018
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
#(a)generate the file
import numpy as np
import cv2
img = cv2.imread('1.jpg',0) #put the image in the ICS4U decitory
#img = np.zeros((512,512,3), np.uint8) #change the size of the image
print(img)
#cv2.imshow('1.jpg',0)
cv2.line(img,(0,1200),(1200,1200),(0,510,0),5)
cv2.line(img,(200,1200),(1200,1200),(510,0,0),5)
cv2.line(img,(400,1200),(1200,1200),(0,0,510),5)
cv2.ellipse(img,(200,200),(100,50),0,0,180,255,-1)
cv2.rectangle(img,(400,0),(0,500),(0,255,0),5)
cv2.circle(img,(1000,700),50,(0,200,0),-1) # draw some lines and ellipses and rectangls into the image
font = cv2.FONT_HERSHEY_SIMPLEX#set the font
cv2.putText(img,'Haking to the Gate',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)#put text to the image within the chosen font
cv2.imwrite('1e.jpg',img)
cv2.imshow('1.jpg',img)
cv2.waitKey(0)
k = cv2.waitKey(0)
if k == 32:
    cv2.destroyAllWindows() 

img2 = cv2.imread('2.jpg',0)#load in a new image
img2 = np.zeros((512,512,3), np.uint8)
#(b)edit it to the  same size with a photograph taken by your phone.
print(img2)
cv2.imshow('2.jpg',0)
for p in range(0,11):
    dst = cv2.addWeighted(img2,1-p/10,img,p/10,0)
    cv2.imwrite('AFTERimage',dst)
    cv2.waitKey(0)
    i = cv2.waitKey(0)
    if i == 32:
        cv2.destroyAllWindows()
