# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Name:Henry
Date: 25/Tan/2018
Program Title: Assignment8:Photo Processing

Purpose: 
(1) Start with the BasicFilter.py program in the Vision Apps repository from GitHub.
(2) Convert the program to work with Python 3 and OpenCV
(3) Use the program to take two similar photos, process them and produce an image that highlights the difference between the photos.



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
    ResultPhotoRaw = np.zeros((X_SIZE,Y_SIZE,3), np.uint8)
    cv2.imwrite("ResultPhoto.PNG",ResultPhotoRaw)
    ResultPhoto=cv2.imread("ResultPhoto.PNG")
    BasePhoto=cv2.imread("BasePhoto.PNG")
    ActivePhoto=cv2.imread("ActivePhoto.PNG")
    #This loop scans through all the pixel in the picture
    for x in range(0, X_SIZE):
        for y in range(0, Y_SIZE):
            Base = BasePhoto[x,y]
            Active = ActivePhoto[x,y]
            if ComparePixels(Base, Active, Tolerance):
                ResultPhoto[x,y] = PositiveColour
            else:
                ResultPhoto[x,y]= NegativeColour
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
    X_Squares = int(X_SIZE/(2*Size+1))
    Y_Squares = int(Y_SIZE/(2*Size+1))
    ResultPhotoRaw = np.zeros((X_SIZE, Y_SIZE,3), np.uint8)
	 #ResultPhotoRaw = Image.new("RGB", (X_SIZE, Y_SIZE), (0,0,0))
    cv2.imwrite("TestSquareOverlay.png",ResultPhotoRaw)
    #ResultPhotoRaw.save("TestSquareOverlay.PNG")
    #draw = ImageDraw.Draw(ResultPhotoRaw)
    ResultPhotoRaw=cv2.imread('Foreground.PNG')#This reads the foreground photo.
    for x in range(0, X_Squares):
        for y in range(0, Y_Squares):
            X = (2*Size+1)*x+Size
            Y = (2*Size+1)*y+Size
            Check = True
            for xi in range(X-Size, X+Size):
                for yi in range(Y-Size, Y+Size):
                    if np.all(ForegroundPhoto[xi,yi] == 255):
                        Check = False
            if Check == False:
                cv2.rectangle(ResultPhotoRaw,(Y-Size,X-Size),(Y+Size,X+Size),(255,255,255),3)
    cv2.imwrite("Testing.PNG",ResultPhotoRaw)
    return ResultPhotoRaw

def photoTaking():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    count = 0
    print("Press SPACE twice to take base and active photoes and press ESC to exit.") #This could give the user some instructions.
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k%256 == 27:
            # When ESC is pressed, the camera will be exited.
            print("The camera will be closed.")
            break
        elif k%256 == 32:
            # When SPACE is pressed, the photo will be taken.
            name = "Photo{}.png".format(count)
            cv2.imwrite(name, frame)
            print("{} written!".format(name))
            count += 1   
    cam.release()
    cv2.destroyAllWindows()


#Take a Base image
photoTaking()

#def getPixel(X, Y)
	#return - RGB colour of Pixel
	#scan photo and compare
ScanRadius = 2 #This checks adjacent pixels
ToleranceBackground = 40 #Set to an arbitrary quantity for later calibration
ToleranceForeground = 2
PositiveColour = [0,0,0] #Black
NegativeColour = [255,255,255] #White

BasePhoto = cv2.imread('Photo0.PNG')
ActivePhoto = cv2.imread('Photo1.PNG')

#Determine the size of the photos
X_SIZE = BasePhoto.shape[0]
Y_SIZE = BasePhoto.shape[1]

cv2.imwrite('BasePhoto.PNG', BasePhoto)
cv2.imwrite('ActivePhoto.PNG', ActivePhoto)


ResultPhotoRaw = np.zeros((X_SIZE,Y_SIZE,3), np.uint8)
ResultPhotoRaw[np.where((ResultPhotoRaw==[0,0,0]).all(axis=2))] = [255,255,255]
cv2.imwrite("ResultPhotoRaw.PNG", ResultPhotoRaw)
#Save a photo processed with ForegroundTolerance:
ForegroundPhotoRaw = ProcessPhoto(BasePhoto, ActivePhoto, ToleranceForeground, PositiveColour, NegativeColour, X_SIZE, Y_SIZE, 'F.PNG') 
cv2.imwrite('Foreground.PNG', ForegroundPhotoRaw)
ForegroundPhoto = cv2.imread('Foreground.PNG')
#ForegroundPhoto = ForegroundPhotoRaw.load()
#Save a photo processed with BackgroundTolerance:
BackgroundPhotoRaw = ProcessPhoto(BasePhoto, ActivePhoto, ToleranceBackground, PositiveColour, NegativeColour, X_SIZE, Y_SIZE, 'B.PNG')
cv2.imwrite('Background.PNG', BackgroundPhotoRaw)

SquareSize = 5
ResultPhoto = SquareOverlay(ForegroundPhoto, BackgroundPhotoRaw, PositiveColour, NegativeColour, SquareSize, X_SIZE, Y_SIZE)

datenow = date.today()
timenow = str(datetime.now()).strip('.')
#print timenow
filename = "Result"+str(ToleranceForeground)+"_"+str(ToleranceBackground)+"_"+str(timenow)+'.PNG'
print (filename)
cv2.imwrite("{0}.png".format(filename),ResultPhoto)






    
    

