#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Name: Angel Kan
Date: January 15, 2018
Program Title: Area Calculator
Program Function: This program calcuates the area under curves (mathematical functions)'''
from math import *
#Variables:
a = 0.0 #This is the starting x value
b = pi #This is the ending x value
n = 1000000 #This is the number of rectangles
Area = 0.0 #This is the total area
#This is the function to use in the area calculation
def f(x):
    return sin(x)
for i in range(1,n+1):
        #Find xi, the current x value
        xi = a + (b - a)/ n * i
        #Find the area of the rectangle, Ai, using the function
        Ai = (b - a)/ n * f(xi)
        #Add it to the total area, "Area"
        Area += Ai
print(Area)

a = 1.0 #starting value
b = 10.0 #ending value
def g(x):
    return 2**x
for i in range(1,n+1):
        xi = a + (b - a)/ n * i  
        Ai = (b - a)/ n * g(xi)
        Area += Ai
print(Area)

a = 0.0 #starting value
b = 100.0 #ending value
def h(x):
    return x**x
for i in range(1,n+1):
        xi = a + (b - a)/ n * i  
        Ai = (b - a)/ n * h(xi)
        Area += Ai
print(Area)

#try to simplify
def f1(x):
    return x
def f2(x):
    return sin(x)
def f3(x):
    return 2**x
function=[f1,f2,f3]#put all functions in a list
def AreaCalculator(a,b,j):
    Area=0.0
    n=100000
    for i in range(1,n+1):
        xi = a + (b - a)/ n * i  
        Ai = (b - a)/ n * function[j](xi)
        Area += Ai
    print(Area)
AreaCalculator(1.0,2.0,0)
AreaCalculator(0.0,pi,1)
AreaCalculator(1.0,10.0,2)