#Robot testing program to determine key features of visual targets
#given the particular ambient lighting conditions.
#Designed for Raspberry Pi co-processors
#This program is designed to have multiple GRIP modules running simultaneously
#This should help FRC teams develop an optimized vision processing system
#For their robots.

#Import modules:
import numpy
import match
from enum import Enum
import GripPipeline
import cv2
import time
from networktables import NetworkTable
import logging
logging.basicConfig(level=logging.DEBUG)

#System specifications:

#Pipe1=GripPipeline1.GripPipeline1()
capture = cv2.VideoCapture(0)


#Photo interval in seconds

#Number of pictures to take
numPictures = 10
#List of GRIP-generated modules to import

#List of base file names for each GRIP processing module.
baseFileName = "photo"
#Loop
for i in range(0,numPictures):
	#Take a picture
	ret, imgFrame = capture.read()
	#Pipe1.process(imgFrame)
	#Process the picture using all required processing schemes
	#Store pictures
	filename=baseFileName+str(i)+".jpg"
	cv2.imwrite(filename,imgFrame)

#Program end: 
#Close connections, etc. 
