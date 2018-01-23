# -*- coding: utf-8 -*-
"""
ChrisLi
Jan 15, 2018
program title: Area calculator
#program functions: This program Calculates the area under curves(mathematical functions)
"""

from math import#
#variables
a = 1.0 #this is the satarting x value 
b = 7.0 #this is the end x value 
n = 10000 #this is the number of rectangles
area = 0.0 #this is the total area

#this is the fuction to use in the area calculation
def f(x):
    return sin(x)
for i in range(1,n+1):
    #Find xi, the current x value
    xi = a + (b-a)/ n * i
    #Find the area of the rectangle Ai
    Ai = (b-a)/ n * f(xi)
    area += Ai
print(area)

a1 = 1.0
b1 = 10.0
def t(x):
    return 2**x
for i in range(1,n+1):
    xi = a1 + (b1-a1)/ n * i
    Ai = (b1 - a1)/ n * t(xi)
    area += Ai
print(area)
    
a2 = 0.0
b2 = pi
def g(x):
    return cos(x)
for i in range(1,n+1):
    xi = a2 + (b2 - a2)/ n * i
    Ai = (b2 - a2)/ n * g(xi)
    area += Ai
print(area)
