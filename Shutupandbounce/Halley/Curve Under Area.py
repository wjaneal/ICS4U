# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:02:56 2018

@author: Halley QIU
Purpose: Area Under Curving
"""
from math import *
# Variables
x1 = 0# This is the starting x value
x2 = pi #This is the ending x value
n = 1000000#This is the number of rectangles
#Those are the total area
Area = 0.0
Areaf1 = 0.0
Areaf2 = 0.0
Areaf3 = 0.0
#This is the functions to use in the area calculation
def f1(x):
    return sin(x)
def f2(x):
    return 2 ** x
def f3(x):
    return x ** 2

for i in range(1, n+1):
# Put the range of f(x)=sinx in the For loop to set the range of x-values
# Find the area of rectangle, Ai    
    for x in range(0, int(pi)):
        #Find the function value
        Aif1 = f1(x1 + (x2 - x1) * i/n) * (x2 - x1) / n
        Areaf1 += Area + Aif1 #Total area, Area
    for x in range(1, 10):
        Aif2 = f2(x1 + (x2 - x1) * i / n) * (x2 - x1) / n
        Areaf2 += Area + Aif2 #Total Area for f(x)=2^x
    for x in range(0, 5):
        Aif3 = f3(x1 + (x2 - x1) * i / n) * (x2 - x1) / n
        Areaf3 += Area + Aif3 #Total area for f(x)=x^2
#Print all the values
print ("x =","x","\n(1)",Areaf1, "\n(2)", Areaf2, "\n(3)", Areaf3)
