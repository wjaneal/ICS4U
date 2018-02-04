#Name:Peter Zeng

#Date: January 25, 2018

#Program Title: Photo Processing

#Program Function:(1) Start with the BasicFilter.py program in the Vision Apps repository from GitHub.
#(2) Convert the program to work with Python 3 and OpenCV
#(3) Use the program to take two similar photos, process them and produce an image that highlights the difference between the photos.
import pygame
import pygame.camera
import pygame.image
from PIL import Image, ImageDraw
from pygame.locals import *


import cv2
import numpy as np
from random import*
from datetime import*
##Setup:
##Graphics modules
#import pygame
#import pygame.camera
#import pygame.image
#from PIL import Image, ImageDraw
#from pygame.locals import *
#from PIL import Image

def ComparePixels(P1,P2,tolerance):
	t1 = abs(P1[0]-P2[0])
	t2 = abs(P1[1]-P2[1])
	t3 = abs(P1[2]-P2[2])
	if t1<= tolerance and t2 <=tolerance and t3 <=tolerance:
		return True
	else:
		return False


def ProcessPhoto(BasePhoto, ActivePhoto, Tolerance, BackgroundColour, ForegroundColour, X_SIZE, Y_SIZE, filename):
    ResultPhotoRaw = np.zeros((X_SIZE,Y_SIZE,3), np.uint8)
    cv2.imwrite("ResultPhoto.PNG",ResultPhotoRaw)
    
    ResultPhoto=cv2.imread("ResultPhoto.PNG")
    BasePhoto=cv2.imread("BasePhoto.PNG")
    ActivePhoto=cv2.imread("ActivePhoto.PNG")

    for x in range(0, Y_SIZE):
        for y in range(0, X_SIZE):
            Base = BasePhoto[x,y]
            Active = ActivePhoto[x,y]
            
            if ComparePixels(Base, Active, Tolerance):
                ResultPhoto[x,y] = ForegroundColour
            else:
                ResultPhoto[x,y]= BackgroundColour
    cv2.imwrite("Testing.PNG",ResultPhoto)
    return ResultPhoto
      

def NeighborhoodScan(ScanRadius, Photo, ForegroundColour, BackgroundColour, x, y):
	Sum = 0
	for X in range(x-ScanRadius, x+ScanRadius):
		for Y in range(y-ScanRadius, y+ScanRadius):
			if Photo[X,Y] == ForegroundColour:
				Sum += 1
			else:
				Sum -= 1
	if Sum >= 0:
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
    X_Squares = int(X_SIZE/(2*Size+1))
    Y_Squares = int(Y_SIZE/(2*Size+1))
    
    TestSquareOverlay = np.zeros((X_SIZE,Y_SIZE,2), np.uint8)
    cv2.imwrite('TestSquareOverlay.PNG',TestSquareOverlay)
    
    #ResultPhoto = ResultPhotoRaw.load()
    ResultPhotoRaw = cv2.imread('TestSquareOverlay.PNG')
    #draw = ImageDraw.Draw(ResultPhotoRaw)
    ResultPhotoRaw = cv2.imread('Foreground.PNG')
    for x in range(0, X_Squares):
        for y in range(0, Y_Squares):
            X = (2*Size+1)*x+Size
            Y = (2*Size+1)*y+Size
			
            Check = True
            for xi in range(X-Size, X+Size):
                for yi in range(Y-Size, Y+Size):
                    if np.all(ForegroundPhoto[xi,yi]) == 0:
                        Check = False
			
            if Check == True:
                cv2.rectangle(ResultPhotoRaw,(X-Size, Y-Size),(X+Size, Y+Size), (255,255,0),1)

                cv2.imwrite('Testing.PNG',ResultPhotoRaw)
                return ResultPhotoRaw

##############################################################################################################################

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()
cv2.destroyAllWindows()

##############################################################################################################################

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    cv2.imshow('frame',hsv)
    k = cv2.waitKey(5) & 0xFF
    if k & 0xFF == ord ('e'):
        cv2.imwrite('TestingPhoto.PNG', hsv)
    if k & 0xFF == ord('e'):
        cv2.imwrite('BasePhotoRaw.PNG',frame)
        if k & 0xFF == ord('e'):
            cv2.imwrite('ActivePhotoRaw.PNG',gray)
            break

cap.release()
cv2.destroyAllWindows()

#############################################################################################################################
def takephotos():
    cam = cv2.videoCapture
    cv2.namedWindow("Camera")
    flag=0
    while True:
        ret, frame = cam.read()
        cv2.imshow("testingPhotos",frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k%256 == 27:
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            if flag == 0:
                img_name = "BasePhotoRaw.PNG"
                cv2.imwrite(img_name, frame)
                flag+=1
            if flag==1:
                img_name = "ActivePhotoRaw.PNG"
                cv2.imwrite(img_name, frame)
                
                
    cv2.destroyAllWindows()
#####################################################################################################################
#Option 1: Process Background and Foreground photos, comparing pixel colours
#Compare the two photos
#for x in range(0+ScanRadius, X_SIZE-ScanRadius):
#	for y in range(0+ScanRadius, Y_SIZE-ScanRadius):
#		#Check the pixel colour of the foreground photo
#		NeighborhoodForeground = NeighborhoodScan(ScanRadius, ForegroundPhoto, 
#PositiveColour, NegativeColour, x, y)
#		#Check the pixel colour of the background photo
#		NeighborhoodBackground = NeighborhoodScan(ScanRadius, BackgroundPhoto, 
#PositiveColour, NegativeColour, x, y)
#		#Make a decision as to the final pixel colour:
#		ResultPhoto[x,y] = PixelDecision(NeighborhoodForeground, 
#NeighborhoodBackground, PositiveColour, NegativeColour)

#Option 2: Use the SquareOverlay Algorithm to fill in the Object on the 
#Background Photo, saving the result 
ScanRadius = 2 #Square 'radius' to check adjacent pixels
ToleranceBackground = 40 #Set to an arbitrary quantity for later calibration
ToleranceForeground = 2
PositiveColour = (0,0,0) #Black
NegativeColour = (255,255,255) #White
SquareSize = 5
ResultPhoto = SquareOverlay(ForegroundPhoto, BackgroundPhotoRaw, PositiveColour, NegativeColour, SquareSize, X_SIZE,Y_SIZE)

datenow = date.today()
timenow = str(datetime.now().strip('.'))
#print timenow
filename = "Result"+str(ToleranceForeground)+"_"+str(ToleranceBackground)+"_"+str(timenow)+'.PNG'
print (filename)
cv2.imwrite("RESULT.png".format_map(filename),ResultPhoto)
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