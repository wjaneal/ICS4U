#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 13:04:25 2018
@author: chenquancheng
"""

#Photo Analysis Program - Isolates an object using a base picture and an active picture
#Modification - filter out noise by combining two pictures processed to optimize background and foreground detection



#Setup:
#Graphics modules
'''
import pygame
import pygame.camera
import pygame.image
from PIL import Image, ImageDraw
from pygame.locals import *
'''
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
    #PositiveColour = ForegroundColour
    #NegativeColour = BackgroundColour
    #BasePhoto = Image.open(BasePhoto)
    #BasePhoto = BasePhoto.load()
    #ActivePhoto = Image.open(ActivePhoto)
    #ActivePhoto = ActivePhoto.load()
    ResultPhotoRaw = np.zeros((height,width,3), np.uint8)
    cv2.imwrite("ResultPhoto.PNG",ResultPhotoRaw)
    ResultPhoto=cv2.imread("ResultPhoto.PNG")
    BasePhoto=cv2.imread("BasePhoto.PNG")
    ActivePhoto=cv2.imread("ActivePhoto.PNG")
    #ResultPhoto = ResultPhotoRaw.load()
    for x in range(0, height):
        for y in range(0, width):
            Base = BasePhoto[x,y]
            Active = ActivePhoto[x,y]
            if ComparePixels(Base, Active, Tolerance):
                ResultPhoto[x,y] = ForegroundColour
                #print(height,width)
                #print(ResultPhoto[x,y])
            else:
                ResultPhoto[x,y]= BackgroundColour
                #print(height,width)
                #print(ResultPhoto[x,y])
    cv2.imwrite("Testing.PNG",ResultPhoto)
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
    print(height,width)
    X_Squares = int(height/(2*Size+1))
    Y_Squares = int(width/(2*Size+1))
    #BackgroundPhoto = cv2.imread('Background.PNG')
    '''TestSquareOverlay = np.zeros((height,width,3), np.uint8)
    cv2.imwrite('TestSquareOverlay.PNG',TestSquareOverlay)
    
    #ResultPhoto = ResultPhotoRaw.load()
    ResultPhotoRaw=cv2.imread('TestSquareOverlay.PNG')
    '''
    ResultPhotoRaw=cv2.imread('Foreground.PNG')
    #draw = ImageDraw.Draw(ResultPhotoRaw)
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
                cv2.rectangle(ResultPhotoRaw,(X-Size, Y-Size),(X+Size, Y+Size),(255,255,255),3)
                #draw.rectangle(((X-Size, Y-Size),(X+Size, Y+Size)), "white")
                #print (X,Y)
                cv2.imwrite("Testing.PNG",ResultPhotoRaw)
    return ResultPhotoRaw
    
	
'''
#Initialize Camera
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
'''
'''cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
'''
 
'''cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    cv2.imshow('frame', rgb)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        out = cv2.imwrite('BasePhotoRaw.PNG', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            out2 = cv2.imwrite('ActivePhotoRaw.PNG', frame)
            break
cap.release()
cv2.destroyAllWindows()
'''
def takePhotos():
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
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            if flag == 0:
        # SPACE pressed
                img_name = "BasePhotoRaw.PNG"
                cv2.imwrite(img_name, frame)
                flag+=1
            if flag==1:
                img_name = "ActivePhotoRaw.PNG"
                cv2.imwrite(img_name, frame)
        
            

    cam.release()

    cv2.destroyAllWindows()



'''#Take a Base image
print ("Please take a photo of the base scene")
input("Please hit any key to take the base photo")
cam.start()
BasePhotoRaw = cam.get_image()
pygame.image.save(BasePhotoRaw, 'BasePhotoRaw.PNG')
cam.stop()
#Take an "Active Image" - with an individual or object in the scene
print ("Please take a photo of the active scene")
input("Please hit any key to take the active photo")
cam.start()
ActivePhotoRaw = cam.get_image()
pygame.image.save(ActivePhotoRaw, 'ActivePhotoRaw.PNG')
cam.stop()
#Determine the size of the photos
X_SIZE = BasePhotoRaw.get_width()
Y_SIZE = BasePhotoRaw.get_height()
print (X_SIZE)
print (Y_SIZE)
'''

''#Take a Base image

print("Please hit space to take the base photo")
print("Please hit space to take the active photo")
takePhotos()







#def getPixel(X, Y)
	#return - RGB colour of Pixel
	#scan photo and compare
ScanRadius = 2 #Square 'radius' to check adjacent pixels
ToleranceBackground = 2 #Set to an arbitrary quantity for later calibration
ToleranceForeground = 40
PositiveColour = [0,0,0] #Black
NegativeColour = [255,255,255] #White

BasePhoto = cv2.imread('BasePhotoRaw.PNG')
ActivePhoto = cv2.imread('ActivePhotoRaw.PNG')
#BasePhoto = BasePhoto.load()
#Determine the size of the photos
height = BasePhoto.shape[0]
width = BasePhoto.shape[1]
'''im_gray = cv2.imread('BasePhotoRaw.PNG', cv2.IMREAD_GRAYSCALE)
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thresh = 127
BasePhoto = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
im_gray = cv2.imread('ActivePhotoRaw.PNG', cv2.IMREAD_GRAYSCALE)
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thresh = 127
ActivePhoto = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
'''
cv2.imwrite('BasePhoto.PNG', BasePhoto)
cv2.imwrite('ActivePhoto.PNG', ActivePhoto)
#ActivePhoto = ActivePhoto.load()

#Prepare the ResultPhoto as a blank white photo
ResultPhotoRaw = np.zeros((height,width,3), np.uint8)
ResultPhotoRaw[np.where((ResultPhotoRaw==[0,0,0]).all(axis=2))] = [255,255,255]
cv2.imwrite("ResultPhotoRaw.PNG", ResultPhotoRaw)
#ResultPhoto = ResultPhoto.load()
#ResultPhoto = ResultPhotoRaw.load()

#Save a photo processed with ForegroundTolerance:
#BasePhoto, ActivePhoto, Tolerance, ForegroundColour, BackgroundColour)
ForegroundPhotoRaw = ProcessPhoto(BasePhoto, ActivePhoto, ToleranceForeground, PositiveColour, NegativeColour, height, width, 'F.PNG') 
cv2.imwrite('Foreground.PNG', ForegroundPhotoRaw)
ForegroundPhoto = cv2.imread('Foreground.PNG')
#ForegroundPhoto = ForegroundPhotoRaw.load()
#Save a photo processed with BackgroundTolerance:
BackgroundPhotoRaw = ProcessPhoto(BasePhoto, ActivePhoto, ToleranceBackground, PositiveColour, NegativeColour, height, width, 'B.PNG')
cv2.imwrite('Background.PNG', BackgroundPhotoRaw)

#BackgroundPhoto = BackgroundPhotoRaw.load()

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
SquareSize = 5
ResultPhoto = SquareOverlay(ForegroundPhoto, BackgroundPhotoRaw, PositiveColour, NegativeColour, SquareSize, height, width)

datenow = date.today()
timenow = str(datetime.now()).strip('.')
#print timenow
filename = "Result"+str(ToleranceForeground)+"_"+str(ToleranceBackground)+"_"+str(timenow)+'.PNG'
print (filename)
cv2.imwrite("{0}.png".format(filename),ResultPhoto)
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