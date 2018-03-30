import numpy
import match
from enum import Enum
import GripPipeline
import cv2

oPipe = GripPipeline.GripPipeline()
imgFrame = cv2.imread('1ftH4ftD1Angle0Brightness.jpg')
oPipe.process(imgFrame)
print oPipe.filter_contours_output
for mxContour in oPipe.filter_contours_output:
	x,y,w,h=cv2.boundingRect(mxContour)
	print("Found: x={} y={} w={} h={}").format(x,y,w,h)
print "Finished"
