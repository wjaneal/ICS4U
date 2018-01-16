#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:27:35 2018

@author: haichunkan
"""
n = 1000000 #This is the number of rectangles
Area = [0.0,0.0,0.0] #This is the total area
#Name: Alice
#Date: January 15, 2018
#Program Title: Area Calculator
#Program Function: This program calcuates the area under curves (mathematical functions)
from math import *
def calculateCurveAreaf():
   #Variables:
    a = 1.0 #This is the starting x value
    b = 5.0 #This is the ending x value
#This is the function to use in the area calculation
    def f(x):
        return x*x
    for i in range(1,n+1):
    #Find xi, the current x value
        xi = a+i*(b-a)/n  
    #Find the area of the rectangle, Ai, using the function
        Aif = f(xi)*(b-a)/n
    #Add it to the total area, "Area"
        Area[0] +=Aif
    #Print the area here
    print("The curve area for f(x) from a to b is",Area[0])    
def calculateCurveAreag():
   #Variables:
    a = 0.0 #This is the starting x value
    b = pi #This is the ending x value
    def g(x):
        return sin(x)
    for i in range(1,n+1):
    #Find xi, the current x value
        xi = a+i*(b-a)/n  
    #Find the area of the rectangle, Ai, using the function
        Aig = g(xi)*(b-a)/n
    #Add it to the total area, "Area"
        Area[1] +=Aig
    #Print the area here
    print("The curve area for g(x) from a to b is",Area[1])
def calculateCurveAreah():
   #Variables:
    a = 1.0 #This is the starting x value
    b = 10.0 #This is the ending x value
    def h(x):
        return 2**x
    for i in range(1,n+1):
    #Find xi, the current x value
        xi = a+i*(b-a)/n  
    #Find the area of the rectangle, Ai, using the function
        Aih = h(xi)*(b-a)/n
    
    #Add it to the total area, "Area"
        Area[2] +=Aih
    #Print the area here
    print("The curve area for g(x) from a to b is",Area[2])
#Run the program.
calculateCurveAreaf()
calculateCurveAreag()
calculateCurveAreah()