# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 13:12:51 2018
@author: Emma
Assignment 8 - Photo Processing

(1) Start with the BasicFilter.py program in the Vision Apps repository from GitHub.
(2) Convert the program to work with Python 3 and OpenCV
(3) Use the program to take two similar photos, process them and produce an 
image that highlights the difference between the photos.

"""
#Photo Analysis Program - Isolates an object using a base picture and an active picture
#Modification - filter out noise by combining two pictures processed to optimize background and foreground detection

#Setup:
#Graphics modulus
#import pygame
#import pygame.camera
#import pygame.image
#from PIL import Image, ImageDraw
#from pygame.locals import *
#Random and Datetime
from random import *
from datetime import *
import numpy as np
import cv2

#Subroutines:
def ComparePixels(P1,P2,tolerance):#tolerance=偏差
    t1 = abs(P1[0]-P2[0])
    t2 = abs(P1[1]-P2[1])
    t3 = abs(P1[2]-P2[2])
    if t1<= tolerance and t2 <=tolerance and t3 <=tolerance:
        return True
    else:
        return False
#Write a function for reading the photos which are used:
def ProcessPhoto(BasePhoto, ActivePhoto, Tolerance, BackgroundColour, 
                 ForegroundColour, X_SIZE, Y_SIZE, filename):
    #PositiveColour = ForegroundColour
    #NegativeColour = BackgroundColour
    #BasePhoto = Image.open(BasePhoto)
    #BasePhoto = BasePhoto.load()
    #ActivePhoto = Image.open(ActivePhoto)
    #ActivePhoto = ActivePhoto.load()
    ResultPhotoRaw = np.zeros((height,width,3), np.uint8)#Create the background of a result photo showing the tolerance
    cv2.imwrite("ResultPhoto.PNG",ResultPhotoRaw)#Save the bcakground
    ResultPhoto=cv2.imread("ResultPhoto.PNG")#Input the final result photo
    BasePhoto=cv2.imread("BasePhoto.PNG")#Input two photos for comparison
    ActivePhoto=cv2.imread("ActivePhoto.PNG")
    #ResultPhoto = ResultPhotoRaw.load()
    #Using a for loop to make the size of the photos same:
    for x in range(0, height):
        for y in range(0, width):#Using a nested loop to combine the range of the sizes together
            Base = BasePhoto[x,y]#Set two variables for the sizes of each photo
            Active = ActivePhoto[x,y]
            if ComparePixels(Base, Active, Tolerance):
                ResultPhoto[x,y] = ForegroundColour#Everything in the result is the foreground color, or
                #print(height,width)
                #print(ResultPhoto[x,y])
            else:
                ResultPhoto[x,y]= BackgroundColour#background color.
                #print(height,width)
                #print(ResultPhoto[x,y])
    cv2.imwrite("Testing.PNG",ResultPhoto)#Save result photo
    return ResultPhoto
#Scanning the area in the photos:
def NeighborhoodScan(ScanRadius, Photo, ForegroundColour, BackgroundColour, x, y):
	#Takes a photo in two RGB colours, ForegroundColour and BackgroundColour 
    #and scans pixels in the neighborhood to determine 
	#to determine whether to keep the pixel colour the same or change it based 
    #on the colours of other nearby pixels
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
'''			
def PixelDecision(NeighborhoodForeground, NeighborhoodBackground, PositiveColour, NegativeColour):
    if NeighborhoodForeground == PositiveColour and NeighborhoodBackground == PositiveColour:#++=+
        return PositiveColour
    elif NeighborhoodForeground == PositiveColour and NeighborhoodBackground == NegativeColour:#+-=+
        return PositiveColour
    elif NeighborhoodForeground == NegativeColour and NeighborhoodBackground == PositiveColour:#-+=+
        return PositiveColour
    else:	
        return NegativeColour#--=-
'''
def PixelDecision(NeighborhoodForeground, NeighborhoodBackground, PositiveColour, NegativeColour):
    if NeighborhoodForeground == NeighborhoodBackground:
        return PositiveColour
    else:	
        return NegativeColour#--=-

def SquareOverlay(ForegroundPhoto, BackgroundPhotoRaw, PositiveColour, NegativeColour, Size, X_SIZE, Y_SIZE):
	#Check for square regions in the Foreground Photo within 'Size' of point 
    #(x,y) that are only of the foreground colour.
	#Paste these into the BackgroundPhoto to create the ResultPhoto
    print(height,width)
    X_Squares = int(height/(2*Size+1))#The area of change
    Y_Squares = int(width/(2*Size+1))
    #BackgroundPhoto = cv2.imread('Background.PNG')
    '''TestSquareOverlay = np.zeros((height,width,3), np.uint8)
    cv2.imwrite('TestSquareOverlay.PNG',TestSquareOverlay)
    
    #ResultPhoto = ResultPhotoRaw.load()
    ResultPhotoRaw=cv2.imread('TestSquareOverlay.PNG')
    '''
    ResultPhotoRaw=cv2.imread('Foreground.PNG')#Input first difference
    #draw = ImageDraw.Draw(ResultPhotoRaw)
    for x in range(0, X_Squares):
        for y in range(0, Y_Squares):#Using a nested loop to set the foreground color for result.
            X = (2*Size+1)*x+Size
            Y = (2*Size+1)*y+Size
		   #print X, Y
            Check = True
            for i in range(X-Size, X+Size):#Outside of the change is black;change is green
                for j in range(Y-Size, Y+Size):
                    if np.all(ForegroundPhoto[i,j] == 255):
                        Check = False
			#If the pixel is white, circle it
            if Check == False:
                cv2.rectangle(ResultPhotoRaw,(X-Size, Y-Size),(X+Size, Y+Size),(255,255,255),3)
                #draw.rectangle(((X-Size, Y-Size),(X+Size, Y+Size)), "white")
                #print (X,Y)
                cv2.imwrite("Testing.PNG",ResultPhotoRaw)#Save the Scanning foreground pic
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
#Using a function to take the pics from camera:
def takePhotos():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Camera")
    flag=0#Set a variable just for giving a permission for saving pics
    while True:
        ret, frame = cam.read()#ret=whether you take the pics=True or False;frame=帧
        cv2.imshow("pic", frame)#Display the pics taken when you click the key
        if not ret:#If the pics are not be taken:
            break#Stop taking pics
        k = cv2.waitKey(1)#Display the pics after 1 sec
        if k%256 == 27:#Press "Esc" to close the camera
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:#Press "Space" to take the pics
            if flag == 0:
        # SPACE pressed
                img_name = "BasePhotoRaw.PNG"
                cv2.imwrite(img_name, frame)#Save the basepic named"basephotoraw"
                flag+=1
            if flag==1:
                img_name = "ActivePhotoRaw.PNG"
                cv2.imwrite(img_name, frame)#At the same time, save the activepic...
                
#When you close the camera, the pics are saved.
        
            
    cv2.destroyAllWindows()#Closing all the windows once you esc



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

print("Please press space to take an base and active photo:")#An instruction for users guiding to take pics
takePhotos()#Start the program for taking pics


#def getPixel(X, Y)
	#return - RGB colour of Pixel
	#scan photo and compare
ScanRadius = 2 #Square 'radius' to check adjacent pixels
ToleranceBackground = 2 #Set to an arbitrary quantity for later calibration
ToleranceForeground = 40
PositiveColour = [0,255,0] #Green
NegativeColour = [0,0,0] #Black

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
ForegroundPhotoRaw = ProcessPhoto(BasePhoto, ActivePhoto, ToleranceForeground, 
                                  PositiveColour, NegativeColour, height, width, 'F.PNG') 
cv2.imwrite('Foreground.PNG', ForegroundPhotoRaw)
ForegroundPhoto = cv2.imread('Foreground.PNG')
#ForegroundPhoto = ForegroundPhotoRaw.load()
#Save a photo processed with BackgroundTolerance:
BackgroundPhotoRaw = ProcessPhoto(BasePhoto, ActivePhoto, ToleranceBackground, 
                                  PositiveColour, NegativeColour, height, width, 'B.PNG')
cv2.imwrite('Background.PNG', BackgroundPhotoRaw)

#BackgroundPhoto = BackgroundPhotoRaw.load()

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
SquareSize = 5
ResultPhoto = SquareOverlay(ForegroundPhoto, BackgroundPhotoRaw, PositiveColour, 
                            NegativeColour, SquareSize, height, width)

datenow = date.today()
timenow = str(datetime.now()).strip('.')
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