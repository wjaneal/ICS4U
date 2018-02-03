'''
Assignment 8 - Photo Processing

Coding convention: 
(a) lower case file name
(b) Name, Date, Title, Purpose in multiline comment at the beginning
(c) mixedCase variable names

(1) Start with the BasicFilter.py program in the Vision Apps repository from GitHub.
(2) Convert the program to work with Python 3 and OpenCV
(3) Use the program to take two similar photos, process them and produce an image that highlights the difference between the photos.
'''

#Import Image Functionality
import pygame
import pygame.camera
import pygame.image
from pygame.locals import *
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()

from PIL import Image

pic_X_size = 6
pic_Y_size = 4

target = (124,129,113)
tolerance = 50

def colour_diff(target, pixel, tolerance):
	if abs(target[0]-pixel[0]) < tolerance and abs(target[1]-pixel[1]) <tolerance and abs(target[2]-pixel[2])<tolerance:
		return True
	else:
		return False

a = []

for row in range(0, pic_Y_size):
	for column in range(0, pic_X_size):

		pixel = (row, column)
		#Take a picture and save it
		image1 = cam.get_image()
		pygame.image.save(image1,'test1'+str(row)+str(column)+'.PNG')
		im = Image.open("test1.PNG") #Can be many different formats.
		pix = im.load()
		pixelcolour = pix[row, column]
		#Get the pixel colour
		if colour_diff(target, pixelcolour, tolerance):
			a.append(pixel)
print a

###############################################################################
import pygame
import pygame.camera
import pygame.image
from pygame.locals import *
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
image1 = cam.get_image()
pygame.image.save(image1,'test1.PNG')
#/usr/share/pyshared/pygame/examples/camera.py ?























































