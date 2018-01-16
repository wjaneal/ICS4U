# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:40:58 2018

@author: Jeffrey 

Purpose:
(1) Find the area under y = sin(x) from x=0 to x = PI.
(2) Find the area under y = 2^x from x = 1 to x = 10
(3) Find the area under a curve of your choice on a range of your choice.
"""
#Program Function: This program calcuates the area under curves (mathematical functions)
from math import *
#Variables:
"""
a = 1.0 #This is the starting x value
b = 5.0 #This is the ending x value
n = 100000 #This is the number of rectangles
Area = 0.0 #This is the total area
"""

#This is the function to use in the area calculation
def f1(x):
    return sin(x)

def f2(x):
    return 2**x

def f3(x):
    return 1/x

a = 0 
b = pi
n = 1000000
Area = 0
for i in range(1,n+1):
    #Find xi, the current x value
    xi = f1(a + i*(b-a)/n)
    #Find the area of the rectangle, Ai, using the function
    Ai = (b-a)/n*xi
    #Add it to the total area, "Area"
    Area += Ai
#Print the area here
print(Area)

a = 1 #This is the starting x value
b = 10 #This is the ending x value
n = 1000000 #This is the number of rectangles
Area = 0 #This is the total area
for i in range(1,n+1):
    #Find xi, the current x value
    xi = f2(a + i*(b-a)/n)
    #Find the area of the rectangle, Ai, using the function
    Ai = (b-a)/n*xi
    #Add it to the total area, "Area"
    Area += Ai
#Print the area here
print(Area)

a = 1 #This is the starting x value
b = 10 #This is the ending x value
n = 1000000 #This is the number of rectangles
Area = 0 #This is the total area
for i in range(1,n+1):
    #Find xi, the current x value
    xi = f3(a + i*(b-a)/n)
    #Find the area of the rectangle, Ai, using the function
    Ai = (b-a)/n*xi
    #Add it to the total area, "Area"
    Area += Ai
#Print the area here
print(Area)









