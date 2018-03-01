
"""
Name: Khan
Date: 20180124
Program Title: assignment7
Purpose: 
(a) Generate a jpg file with the following: Rectangles, dots, text, ellipses and lines of different colours.
(b) Take a second .jpg file and edit it to the  same size with a photograph taken by your phone.
(c) Blend the two together in 11 jpg photographs ranging from 0-100%, 10-90%, ... all the way to 100-0%
Variable names:Img1,Img2,Height,Width,Res,Mix
"""
import cv2
import numpy as np#This is to import the module
Img1 = cv2.imread('BasePhotoRaw.PNG')#This is to read the image
Img2 = cv2.imread('ResultPhoto.PNG')#This is to read another image
'''
Though actually that's a photograph in my phone instead of one taken by it(img2)
I like the characters ...and want to use this picture

'''
cv2.imwrite('1.jpg',Img1)#This is to rewrite the first image
Img1 = np.zeros((800,800,3), np.uint8)#This is to set the size of the picture
cv2.line(Img1,(0,400),(51,51),(25,366,0),5)#This is to draw a line
cv2.rectangle(Img1,(100,100),(300,300),(0,25,399),10)#This is to draw a rectangle
cv2.ellipse(Img1, (300, 200), (100, 50), 20, 30, 70, (255,0,0), 6)#This is to draw a ellipse
font = cv2.FONT_HERSHEY_SIMPLEX#This is to choose a font
cv2.putText(Img1,'6666666hhhhhhhh6666666',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)#This is to write some texts

Height, Width = Img1.shape[:2]#This is to get the size of the picture
Res = cv2.resize(Img2,(Width, Height), interpolation = cv2.INTER_CUBIC)#This is to change the size of the second picture

for i in range (0,11):#This is to start a loop
    Mix = cv2.addWeighted(Img1, i/10, Res, 1-i/10, 0)#This is to mix the pictures
    cv2.imwrite('picture'+str(i+1)+'.jpg',Mix)#This is to save the pictures down
    






