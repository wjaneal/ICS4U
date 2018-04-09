#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 13:11:55 2018

@author: haichunkan
"""

#Setup:
#Graphics modules


#from random import *
#rom datetime import *

import numpy as np
import cv2
#import datetime


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
        PositiveColour = ForegroundColour
        NegativeColour = BackgroundColour
        
        ResultPhotoRaw = np.zeros((X_SIZE, Y_SIZE,3), np.uint8)
        ResultPhotoRaw[:]=(255,255,255)
        
      
        cv2.imwrite("ResultPhotoRaw.jpg", ResultPhotoRaw)

        ResultPhoto=cv2.imread('ResultPhotoRaw.jpg')
        
        for x in range(0, X_SIZE):
            for y in range(0, Y_SIZE):
                Base = BasePhoto[x,y]
                Active = ActivePhoto[x,y]
                if ComparePixels(Base, Active, Tolerance):
                    ResultPhoto[x,y] = PositiveColour
                else:
                    ResultPhoto[x,y]= NegativeColour
                    
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
    X_Squares = int(X_SIZE/(2*Size+1))
    Y_Squares = int(Y_SIZE/(2*Size+1))
    ResultPhotoRaw = np.zeros((X_SIZE, Y_SIZE,3), np.uint8)
    ResultPhotoRaw[:]=(255,255,255)
    
    cv2.imwrite("TestSquareOverlay.png",ResultPhotoRaw)
    
    for x in range(0, X_Squares):
        for y in range(0, Y_Squares):
            
            X = (2*Size+1)*x+Size
            Y = (2*Size+1)*y+Size
		   #print X, Y
            Check = True
            for xi in range(X-Size, X+Size):
                for yi in range(Y-Size, Y+Size):
                
                    if np.all(ForegroundPhoto[xi,yi] == 255):
                        Check = False
            if Check == False:
                #This creates a rectangle.
                cv2.rectangle(ResultPhotoRaw,(X-Size, Y-Size),(X+Size, Y+Size),(255,255,255),3)
    cv2.imwrite("Testing.PNG",ResultPhotoRaw)#This saves the photo.
    return ResultPhotoRaw
	

#Initialize Camera


#Take a Base image
#print ("Please take a photo of the base scene")
#input("Please hit any key to take the base photo")

cap = cv2.VideoCapture(0)

#img_counter = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        #SPACE pressed
        #img_name = "BasePhotoRaw.png"
        cv2.imwrite("BasePhotoRaw.png", frame)
        #print("{} written!".format(img_name))
        #img_counter += 1
        cv2.destroyAllWindows()
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


#Take an "Active Image" - with an individual or object in the scene
#print ("Please take a photo of the active scene")
#input("Please hit any key to take the active photo")

cap = cv2.VideoCapture(0)

#img_counter = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    # Display the resulting frame
    cv2.imshow('ActivePhotoRaw.png',frame)
    if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y'
        # SPACE pressed
        #img_name = "ActivePhotoRaw.png".format(img_counter)
        cv2.imwrite("ActivePhotoRaw.png", frame)
        #print("{} written!".format(img_name))
        #img_counter += 1
        cv2.destroyAllWindows()
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


#Determine the size of the photos
BasePhotoRaw = cv2.imread ("ActivePhotoRaw.png")
X_SIZE, Y_SIZE = BasePhotoRaw.shape[:2]
#X_SIZE = BasePhotoRaw.get_width()
#Y_SIZE = BasePhotoRaw.get_height()
#print (X_SIZE) #X_SIZE
#print (Y_SIZE)#Y_SIZE

#def getPixel(X, Y)
	#return - RGB colour of Pixel
	#scan photo and compare
ScanRadius = 2 #Square 'radius' to check adjacent pixels
ToleranceBackground = 30 #Set to an arbitrary quantity for later calibration
ToleranceForeground = 2
PositiveColour = [0,0,0] #Black
NegativeColour = [255,255,255] #White

BasePhoto = cv2.imread('BasePhotoRaw.png')
#cv2.imshow('BasePhotoRaw.png', BasePhoto)

ActivePhoto = cv2.imread('ActivePhotoRaw.png')
#cv2.imshow('ActivePhotoRaw.png', ActivePhoto)

#Prepare the ResultPhoto as a blank white photo
ResultPhotoRaw = np.zeros((X_SIZE, Y_SIZE,3), np.uint8)
ResultPhotoRaw[:] = (255, 255, 255)

cv2.imwrite("ResultPhotoRaw.png",ResultPhotoRaw)
#ResultPhotoRaw.save("ResultPhotoRaw.PNG")
ResultPhoto = cv2.imread ("ResultPhotoRaw.png")
#cv2.imshow('ResultPhotoRaw.png', ResultPhoto)


#Save a photo processed with ForegroundTolerance:
#BasePhoto, ActivePhoto, Tolerance, ForegroundColour, BackgroundColour)
ForegroundPhotoRaw = ProcessPhoto(BasePhoto, ActivePhoto, ToleranceForeground, PositiveColour, NegativeColour, X_SIZE, Y_SIZE, 'F.PNG') 
cv2.imwrite('Foreground.png', ForegroundPhotoRaw)
#ForegroundPhotoRaw.save('Foreground.PNG')
#cv2.imshow('Foreground.png', ForegroundPhotoRaw)
ForegroundPhoto = cv2.imread ("Foreground.png")
#ForegroundPhoto = ForegroundPhotoRaw.load()
#Save a photo processed with BackgroundTolerance:
BackgroundPhotoRaw = ProcessPhoto(BasePhoto, ActivePhoto, ToleranceBackground, PositiveColour, NegativeColour, X_SIZE, Y_SIZE, 'B.PNG')
cv2.imwrite('Background.png', BackgroundPhotoRaw)
#BackgroundPhotoRaw.save('Background.PNG')
#cv2.imshow('Background.png', BackgroundPhotoRaw)
#BackgroundPhoto = cv2.imread ("Background.png")
#BackgroundPhoto = BackgroundPhotoRaw.load()

#Option 1: Process Background and Foreground photos, comparing pixel colours
#Compare the two photos
'''
for x in range(0+ScanRadius, X_SIZE-ScanRadius):
	for y in range(0+ScanRadius, Y_SIZE-ScanRadius):
		#Check the pixel colour of the foreground photo
		NeighborhoodForeground = NeighborhoodScan(ScanRadius, ForegroundPhoto, PositiveColour, NegativeColour, x, y)
		#Check the pixel colour of the background photo
		NeighborhoodBackground = NeighborhoodScan(ScanRadius, BackgroundPhoto, PositiveColour, NegativeColour, x, y)
		#Make a decision as to the final pixel colour:
		ResultPhoto[x,y] = PixelDecision(NeighborhoodForeground, NeighborhoodBackground, PositiveColour, NegativeColour)
'''
#Option 2: Use the SquareOverlay Algorithm to fill in the Object on the Background Photo, saving the result 
SquareSize = 5
ResultPhoto = SquareOverlay(ForegroundPhoto, BackgroundPhotoRaw, PositiveColour, NegativeColour, SquareSize, X_SIZE, Y_SIZE)

#datenow = datetime.now()
#timenow = str(datetime.now()).strip('.')
#print timenow
#filename = "Result"+str(ToleranceForeground)+"_"+str(ToleranceBackground)+"_"+str(timenow)+'.PNG'
#print (filename)
#ResultPhotoRaw.save(filename)

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