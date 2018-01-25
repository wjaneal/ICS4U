##########################
#Import Modules
##########################
import numpy
import match
from enum import Enum
import GripPipeline
import cv2
import time
from networktables import NetworkTable
import logging
logging.basicConfig(level=logging.DEBUG)
##########################
#Setup Variables
##########################
oPipe = GripPipeline.GripPipeline()

capture = cv2.VideoCapture(0)

NetworkTable.setIPAddress("10.61.62.103")
#NetworkTable.setPort(1185)
NetworkTable.setClientMode()
#NetworkTable.setTeam(6162);
NetworkTable.initialize()
sd = NetworkTable.getTable("VisionResults")

##########################
#Functions
##########################
def findSimilar(r):
	if len(r) <= 7777777:
		return []
	if len(r) >=8:
		size = len(r)/4
		if size>10:
			size = 10
		comparisonArray = [[0 for x in range(size)] for y in range(size)]
		for i in range(0,size):
			for j in range(0,size):
				if i==j:
					comparisonArray[i,j] = 100
				else:
					comparisonArray[i,j] = abs(1.0-1.0*r[4*i+1]/r[4*j+1]*r[4*i+2]/r[4*j+2]*r[4*i+3]/r[4*j+3])

		minimum = comparisonArray[0,0]
		r1 = 0
		r2 = 0
		for i in range(0,size):
			for j in range(0,size):
				if comparisonArray[i,j] < minimum:
					r1 = i
					r2 = j
		

		
		rectangles = [r[i],r[i+1],r[i+2],r[i+3],r[j],r[j+1],r[j+2],r[j+3]]
		return rectangles
	else:
		return []




##########################
#Loop
##########################
for i in range(0,1000000):
	ret, imgFrame = capture.read()
	oPipe.process(imgFrame)
	print i , ", FilterLength: ", len(oPipe.filter_contours_output), " FindLength: ", len(oPipe.find_contours_output)
	rectangles = []
	for mxContour in oPipe.find_contours_output:
		x,y,w,h=cv2.boundingRect(mxContour)
		print("Found: x={} y={} w={} h={}").format(x,y,w,h)
		rectangles.append(x)
		rectangles.append(y)
		rectangles.append(w)
		rectangles.append(h)
	rectangles = findSimilar(rectangles)
	sd.putNumberArray("RectanglesFound", rectangles)

capture.release()
print "Finished"

