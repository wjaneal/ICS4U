# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 01:00:28 2018

@author: simet
"""
import numpy as np
import cv2
import time

def ComparePixels(P1,P2,tolerance):
    t1 = abs(P1[0]-P2[0])
    t2 = abs(P1[1]-P2[1])
    t3 = abs(P1[2]-P2[2])
    if t1<= tolerance and t2 <=tolerance and t3 <=tolerance:
        return True
    else:
        return False

def ProcessPhoto(BasePhoto, ActivePhoto, Tolerance, BackgroundColour, ForegroundColour,w,h, filename):
    PositiveColour = ForegroundColour
    NegativeColour = BackgroundColour
    for x in range(0, w):
        for y in range(0, h):
            Base = BasePhoto[x,y]
            Active = ActivePhoto[x,y]
            if ComparePixels(Base, Active, Tolerance):
                ResultPhoto[x,y] = PositiveColour
            else:
                ResultPhoto[x,y]= NegativeColour
                
    cv2.imwrite("Testing.PNG",ResultPhoto)
    return ResultPhoto

def NeighborhoodScan(ScanRadius, Photo, ForegroundColour, BackgroundColour, x, y):
    Sum = 0
    for X in range(x-ScanRadius, x+ScanRadius):
        for Y in range(y-ScanRadius, y+ScanRadius):
            if Photo[X,Y] == ForegroundColour:
                Sum+=1
            else:
                Sum-=1
                
    if Sum >=0:
        return ForegroundColour
    else:
        return BackgroundColour		
			
def PixelDecision(NeighborhoodForeground, NeighborhoodBackground, PositiveColour, NegativeColour):
    if NeighborhoodForeground == PositiveColour and NeighborhoodBackground == PositiveColour:
        return PositiveColour
    elif NeighborhoodForeground == PositiveColour and NeighborhoodBackground == NegativeColour:
        return PositiveColour
    elif NeighborhoodForeground == NegativeColour and NeighborhoodBackground == PositiveColour:
        return PositiveColour
    else:	
        return NegativeColour

def SquareOverlay(ForegroundPhoto, BackgroundPhotoRaw, PositiveColour, NegativeColour, Size,w, h):
    X_Squares = int(w/(2*Size+1))
    Y_Squares = int(h/(2*Size+1))
    
    Blackphoto = np.zeros((w,h,3), np.uint8)
    cv2.imwrite('Blackphoto.PNG',Blackphoto)
    ResultPhotoRaw=cv2.imread('Foreground.PNG')
    for x in range(0, X_Squares):
        for y in range(0, Y_Squares):
            X = (2*Size+1)*x+Size
            Y = (2*Size+1)*y+Size
            Check = True
            for xi in range(X-Size, X+Size):
                for yi in range(Y-Size, Y+Size):
                    #This checks if the pixel is white.
                    if np.all(ForegroundPhoto[xi,yi] == 255):
                        Check = False
            if Check == False:
                #This creates a rectangle.
                cv2.rectangle(ResultPhotoRaw,(Y-Size,X-Size),(Y+Size,X+Size),(255,255,255),3)
    cv2.imwrite("Testing.PNG",ResultPhotoRaw)#This saves the photo.
    return ResultPhotoRaw
	

#Determine the size of the photos
def pz():
    photo = np.zeros((640,480,3), np.uint8)
    photo = cv2.VideoCapture(0)
    while(True):
        ret, frame = photo.read()
        cv2.imshow("", frame)
        if not ret:
                break
        k = cv2.waitKey(1)
        if k==99:
            break
            
        if  k == 97:
                   ret, BasePhotoRaw = photo.read()
                   cv2.imshow("photo", BasePhotoRaw)
                   cv2.imwrite("BasePhotoRaw.PNG", BasePhotoRaw)
        if k==98:
                    ret, BasePhotoRaw = photo.read()
                    cv2.imshow("photo", BasePhotoRaw)
                    cv2.imwrite("ActivePhotoRaw.PNG", BasePhotoRaw)
                    break
    photo.release()
    cv2.destroyAllWindows()
    
print('take two pictures by pressing a and b,exit by c')
pz()

BasePhoto = cv2.imread('BasePhotoRaw.PNG')
ActivePhoto = cv2.imread('ActivePhotoRaw.PNG')
w = BasePhoto.shape[0]
h = BasePhoto.shape[1]
print(w,h)
ScanRadius = 2
ToleranceBackground = 40
ToleranceForeground = 2
PositiveColour = [0,0,0] 
NegativeColour = [255,255,255]

cv2.imwrite('BasePhoto.PNG', BasePhoto)
cv2.imwrite('ActivePhoto.PNG', ActivePhoto)
ResultPhotoRaw = np.zeros((w,h,3), np.uint8)
ResultPhotoRaw[np.where((ResultPhotoRaw==[0,0,0]).all(axis=2))] = [255,255,255]
cv2.imwrite("ResultPhotoRaw.PNG", ResultPhotoRaw)
cv2.imwrite("ResultPhoto.PNG",ResultPhotoRaw)

ResultPhoto=cv2.imread("ResultPhoto.PNG")

ForegroundPhotoRaw = ProcessPhoto(BasePhoto, ActivePhoto, ToleranceForeground, PositiveColour, NegativeColour, w, h, 'F.PNG') 
cv2.imwrite('Foreground.PNG', ForegroundPhotoRaw)
ForegroundPhoto = cv2.imread('Foreground.PNG')
BackgroundPhotoRaw = ProcessPhoto(BasePhoto, ActivePhoto, ToleranceBackground, PositiveColour, NegativeColour, w, h, 'B.PNG')
cv2.imwrite('Background.PNG', BackgroundPhotoRaw)
SquareSize = 5
ResultPhoto = SquareOverlay(ForegroundPhoto, BackgroundPhotoRaw, PositiveColour, NegativeColour, SquareSize, w, h)
timenow = time.strftime("%Y%m%d%H%M%S")
filename = "Result"+str(ToleranceForeground)+"_"+str(ToleranceBackground)+"_"+str(timenow)+'.PNG'
print (filename)
cv2.imwrite("{0}.png".format(filename),ResultPhoto)
