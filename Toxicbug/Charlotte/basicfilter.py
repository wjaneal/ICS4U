#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: chenquancheng
Date: Created on Thu Jan 25 13:04:25 2018
Title: Image Processing
Purpose: Use the program to take two similar photos, process them and produce an image that highlights the difference between the photos.
"""

#Photo Analysis Program - Isolates an object using a base picture and an active picture
#Modification - filter out noise by combining two pictures processed to optimize background and foreground detection



#Setup:
#Graphics modules
import numpy as np
import cv2
#Random and Datetime
from random import *
from datetime import *


#Subroutines:
def ComparePixels(P1,P2,tolerance):
    t1 = abs(P1[0]-P2[0])
    t2 = abs(P1[1]-P2[1])
    t3 = abs(P1[2]-P2[2])
    if t1<= tolerance and t2 <=tolerance and t3 <=tolerance:
        return True
    else:
        return False

def ProcessPhoto(BasePhoto, ActivePhoto, Tolerance, BackgroundColour, ForegroundColour, X_SIZE, Y_SIZE, filename):
    ResultPhotoRaw = np.zeros((height,width,3), np.uint8)#This creates a new image.
    cv2.imwrite("ResultPhoto.PNG",ResultPhotoRaw)#This saves the new image.
    ResultPhoto=cv2.imread("ResultPhoto.PNG")#This reads the image.
    BasePhoto=cv2.imread("BasePhoto.PNG")#This reads the base photo.
    ActivePhoto=cv2.imread("ActivePhoto.PNG")#This reads the active photo.
    #This loop iterates through each pixel in the base and active photos.
    for x in range(0, height):
        for y in range(0, width):
            Base = BasePhoto[x,y]
            Active = ActivePhoto[x,y]
            #This compares the color of the pixels of these two photos.
            if ComparePixels(Base, Active, Tolerance):
                ResultPhoto[x,y] = ForegroundColour
            else:
                ResultPhoto[x,y]= BackgroundColour
    cv2.imwrite("Testing.PNG",ResultPhoto)#This saves the photo.
    return ResultPhoto

def NeighborhoodScan(ScanRadius, Photo, ForegroundColour, BackgroundColour, x, y):
	#Takes a photo in two RGB colours, ForegroundColour and BackgroundColour and scans pixels in the neighborhood to determine 
	#to determine whether to keep the pixel colour the same or change it based on the colours of other nearby pixels
    Sum = 0
	#The following nested loop adds one for Foreground Colour and Subtracts one for background colour
    for X in range(x-ScanRadius, x+ScanRadius):
        for Y in range(y-ScanRadius, y+ScanRadius):
            if Photo[X,Y] == ForegroundColour:
                Sum+=1
            else:
                Sum-=1
	#If the sum is positive, then the foreground colour wins and vice versa
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

def SquareOverlay(ForegroundPhoto, BackgroundPhotoRaw, PositiveColour, NegativeColour, Size, X_SIZE, Y_SIZE):
	#Check for square regions in the Foreground Photo within 'Size' of point (x,y) that are only of the foreground colour.
	#Paste these into the BackgroundPhoto to create the ResultPhoto
    #print(height,width)
    X_Squares = int(height/(2*Size+1))
    Y_Squares = int(width/(2*Size+1))
    #BackgroundPhoto = cv2.imread('Background.PNG')
    '''TestSquareOverlay = np.zeros((height,width,3), np.uint8)
    cv2.imwrite('TestSquareOverlay.PNG',TestSquareOverlay)
    
    #ResultPhoto = ResultPhotoRaw.load()
    ResultPhotoRaw=cv2.imread('TestSquareOverlay.PNG')
    '''
    ResultPhotoRaw=cv2.imread('Foreground.PNG')#This reads the foreground photo.
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
    
def takePhotos():
    #This function takes photos with the computer's camera and saves them.
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Camera")
    flag=0
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k%256 == 27:
            #This exits the camera when pressing ESC.
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            if flag == 0:
                img_name = "BasePhotoRaw.PNG" #This lets the camera take a photo when pressing SPACE.
                cv2.imwrite(img_name, frame)#This saves the photo.
                flag+=1
            if flag==1:
                img_name = "ActivePhotoRaw.PNG"
                cv2.imwrite(img_name, frame)
    cam.release()
    cv2.destroyAllWindows()

#These give the user some instructions when taking photos.
print("Please hit space to take the base photo")
print("Please hit space to take the active photo")
takePhotos()
ScanRadius = 2 #Square 'radius' to check adjacent pixels
ToleranceBackground = 2 #Set to an arbitrary quantity for later calibration
ToleranceForeground = 40
PositiveColour = [0,0,0] #Black
NegativeColour = [255,255,255] #White
BasePhoto = cv2.imread('BasePhotoRaw.PNG')#This reads the base photo.
ActivePhoto = cv2.imread('ActivePhotoRaw.PNG')#This reads the active photo.
#This determines the size of the photo.
height = BasePhoto.shape[0]
width = BasePhoto.shape[1]
cv2.imwrite('BasePhoto.PNG', BasePhoto)
cv2.imwrite('ActivePhoto.PNG', ActivePhoto)
#This prepares the ResultPhoto as a blank white photo
ResultPhotoRaw = np.zeros((height,width,3), np.uint8)
ResultPhotoRaw[np.where((ResultPhotoRaw==[0,0,0]).all(axis=2))] = [255,255,255]
cv2.imwrite("ResultPhotoRaw.PNG", ResultPhotoRaw)
#This saves a photo processed with ForegroundTolerance:
ForegroundPhotoRaw = ProcessPhoto(BasePhoto, ActivePhoto, ToleranceForeground, PositiveColour, NegativeColour, height, width, 'F.PNG') 
cv2.imwrite('Foreground.PNG', ForegroundPhotoRaw)
ForegroundPhoto = cv2.imread('Foreground.PNG')
#This saves a photo processed with BackgroundTolerance:
BackgroundPhotoRaw = ProcessPhoto(BasePhoto, ActivePhoto, ToleranceBackground, PositiveColour, NegativeColour, height, width, 'B.PNG')
cv2.imwrite('Background.PNG', BackgroundPhotoRaw)

#Option 1: Process Background and Foreground photos, comparing pixel colours
#Compare the two photos
#for x in range(0+ScanRadius, X_SIZE-ScanRadius):
#	for y in range(0+ScanRadius, Y_SIZE-ScanRadius):
#		#Check the pixel colour of the foreground photo
#		NeighborhoodForeground = NeighborhoodScan(ScanRadius, ForegroundPhoto, PositiveColour, NegativeColour, x, y)
#		#Check the pixel colour of the background photo
#		NeighborhoodBackground = NeighborhoodScan(ScanRadius, BackgroundPhoto, PositiveColour, NegativeColour, x, y)
#		#Make a decision as to the final pixel colour:
#		ResultPhoto[x,y] = PixelDecision(NeighborhoodForeground, NeighborhoodBackground, PositiveColour, NegativeColour)

#Option 2: Use the SquareOverlay Algorithm to fill in the Object on the Background Photo, saving the result 
SquareSize = 1
ResultPhoto = SquareOverlay(ForegroundPhoto, BackgroundPhotoRaw, PositiveColour, NegativeColour, SquareSize, height, width)

datenow = date.today()
timenow = str(datetime.now()).strip('.')
#print timenow
filename = "Result"+str(ToleranceForeground)+"_"+str(ToleranceBackground)+"_"+str(timenow)+'.PNG'
print (filename)
cv2.imwrite("{0}.png".format(filename),ResultPhoto)

#analyse data set
#Check (Xav,Yav):
	#whole photo
	#horizontal stripes
	#vertical stripes
	#store in an array
	#Maximum range of horizontal and vertical change
#Compare current array to last several arrays
	#note differences in horizontal and vertical stripe averages with respect to whole picture
#make some decision based on this.
