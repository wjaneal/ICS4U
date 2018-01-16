# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 02:25:04 2018

@author: 11256
"""

#Name: Tony
#Date: January 15, 2018
#Program Title: Area Calculator
#Program Function: This program calcuates the area under curves (mathematical functions)
from math import *
#Variables:
x = 0.0 #This is the starting x value
x1 = 3.1 #This is the ending x value
n = 1000000 #This is the number of rectangles
Area = 0.0 #This is the total area

#This is the function to use in the area calculation
def f(x):
    return (sin(x))


for i in range(1,n+1):
    #Find xi, the current x value
    xi = (x+((x1-x)/n)*i)
    #Find the area of the rectangle, Ai, using the function
    Ai = (x+((x1-x)/n)*i)*((x1-x)/n)
    #Add it to the total area, "Area"
    Area += Ai
print (Area)
#Print the area here

a = 1.0
b = 10.0
n = 1000000
Area = 0.0

def f(a):
    return (2**a)

for i in range(1,n+1):
    #Find xi, the current x value
    xi = (a+((b-a)/n)*i)
    #Find the area of the rectangle, Ai, using the function
    Ai = (a+((b-a)/n)*i)*((b-a)/n)
    #Add it to the total area, "Area"
    Area += Ai
print (Area)

a = 5.0
b = 10.0
n = 1000000
Area = 0.0

def f(a):
    return (2**a*2)

for i in range(1,n+1):
    #Find xi, the current x value
    xi = (a+((b-a)/n)*i)
    #Find the area of the rectangle, Ai, using the function
    Ai = (a+((b-a)/n)*i)*((b-a)/n)
    #Add it to the total area, "Area"
    Area += Ai
print (Area)


