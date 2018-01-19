# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:02:56 2018

@author: Halley QIU
Purpose: Area Under Curving
"""
from math import *
# Variables
a = 0.0 # This is the starting x value
b = 4 * atan(1) #This is the ending x value
n = 1000000 #This is the number of rectangles

Area = 0.0#This is the total area

#This is the functions to use in the area calculation
def f1(x):
    return sin(x)
for i in range(1, n+1):
    xi = a + (b - a)/ n * i # Ai is the current x value
    Ai = (b - a) / n * f1(xi) # the Area of Rectangle, Ai
    Area += Ai# Add to the total area
print(Area)

a = 1.0
b = 10.0
def f2(x):
    return 2 ** x
for i in range(1, n+1):
    xi = a + (b - a) / n * i
    Ai = (b-a) / n * f2(xi)
    Area += Ai
print(Area)

a = 0.0
b = 5.0
def f3(x):
    return x ** 2
for i in range(1, n+1):
    xi = a + (b - a) / n * i
    Ai = (b - a) / n * f3(xi)
    Area += Ai
print(Area)