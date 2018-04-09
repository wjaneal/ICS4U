# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 01:00:28 2018

@author: simet
"""
import datetime
import cv2
import numpy as np


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
        #BasePhoto = Image.open(BasePhoto)
        #BasePhoto = BasePhoto.load()
        #ActivePhoto = Image.open(ActivePhoto)
        #ActivePhoto = ActivePhoto.load()
        ResultPhotoRaw = np.zeros((X_SIZE, Y_SIZE,3), np.uint8)
        ResultPhotoRaw[:]=(255,255,255)
        #ResultPhotoRaw[:,0:0.5*X_SIZE] = (255,255,255)
        #ResultPhotoRaw[:,0.5*X_SIZE:Y_SIZE] = (255,255,255)
        #ResultPhotoRaw = Image.new("RGB", (X_SIZE, Y_SIZE), (255,255,255))
        cv2.imwrite("ResultPhotoRaw.jpg",ResultPhotoRaw)
        #ResultPhotoRaw.save(filename)
        ResultPhoto = cv2.imread('ResultPhotoRaw.jpg')
        for x in range(0, X_SIZE):
                for y in range(0, Y_SIZE):
                        Base = BasePhoto[x,y]
                        Active = ActivePhoto[x,y]
                        if ComparePixels(Base, Active, Tolerance):
                                ResultPhoto[x,y] = PositiveColour
                        else:
                                ResultPhoto[x,y] = NegativeColour
                cv2.imwrite("Testing.PNG",ResultPhoto)
        return ResultPhotoRaw

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
    cv2.imwrite('TestSquareOverlay.PNG',ResultPhotoRaw)
        #ResultPhotoRaw.save("TestSquareOverlay.PNG")
    ResultPhoto = cv2.imread('TestSquareOverlay.PNG',0)
        #ResultPhoto = ResultPhotoRaw.load()
    #draw = ImageDraw.Draw(ResultPhotoRaw)
    for x in range(0, X_Squares):
        for y in range(0, Y_Squares):
            X = (2*Size+1)*x+Size
            Y = (2*Size+1)*y+Size
			#print X, Y
            #Check = True
            while True:
                for xi in range(X-Size, X+Size):
                    for yi in range(Y-Size, Y+Size):
                        if ForegroundPhoto[xi,yi] == NegativeColour:
                            return True
			
                        if False:
                            cv2.rectangle(ResultPhoto,(X-Size, Y-Size),(X+Size, Y+Size),(255,255,255),3)
				          #draw.rectangle(((X-Size, Y-Size),(X+Size, Y+Size)), "white")
                    print (X,Y)
        cv2.imwrite("Testing.PNG",ResultPhotoRaw)
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

ScanRadius = 2 
ToleranceBackground = 40
ToleranceForeground = 2
PositiveColour = [0,0,0] 
NegativeColour = [255,255,255]

BasePhoto = cv2.imread('BasePhotoRaw.PNG')
cv2.imshow('BasePhotoRaw.PNG',BasePhoto)
ActivePhoto = cv2.imread('ActivePhotoRaw.PNG')
cv2.imshow('ActivePhotoRaw.PNG',ActivePhoto)
#BasePhoto = BasePhoto.load()
w = BasePhoto.shape[0]
h = BasePhoto.shape[1]

cv2.imwrite('BasePhoto.PNG', BasePhoto)
cv2.imwrite('ActivePhoto.PNG', ActivePhoto)
#ActivePhoto = ActivePhoto.load()
ResultPhotoRaw = np.zeros((w,h,3), np.uint8)
ResultPhotoRaw[:]=(255,255,255)
cv2.imwrite("ResultPhotoRaw.PNG",ResultPhotoRaw)
ResultPhoto = cv2.imread('ResultPhotoRaw.PNG',0)
cv2.imshow('ResultPhoto.PNG',ResultPhoto)
cv2.imshow('ResultPhotoRaw.PNG',ResultPhoto)
#ResultPhoto = ResultPhoto.load()
#ResultPhoto = ResultPhotoRaw.load()
ForegroundPhotoRaw = ProcessPhoto(BasePhoto, ActivePhoto, ToleranceForeground, PositiveColour, NegativeColour,w,h, 'F.PNG') 
ForegroundPhotoRaw = cv2.imwrite('Foreground.PNG',ForegroundPhotoRaw)
ForegroundPhoto = cv2.imshow('1',ForegroundPhotoRaw)

BackgroundPhotoRaw = ProcessPhoto(BasePhoto, ActivePhoto, ToleranceBackground, PositiveColour, NegativeColour,w,h, 'B.PNG')
BackgroundPhotoRaw = cv2.imwrite('Background.PNG',BackgroundPhotoRaw)
BackgroundPhoto = cv2.imshow('2',BackgroundPhotoRaw)

SquareSize = 5
ResultPhoto = SquareOverlay(ForegroundPhoto, BackgroundPhotoRaw, PositiveColour, NegativeColour, SquareSize, w, h)

datenow = datetime.today()
timenow = str(datetime.now()).strip('.')
#print timenow
filename = "Result"+str(ToleranceForeground)+"_"+str(ToleranceBackground)+"_"+str(timenow)+'.PNG'
print (filename)
cv2.imwrite(filename,ResultPhotoRaw)
