# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:07:24 2018

@author: Emma
Program Title: Area Calculator
Function: This program calculates the area under curves
(1) Find the area under y = sin(x) from x=0 to x = PI.
(2) Find the area under y = 2^x from x = 1 to x = 10
(3) Find the area under a curve of your choice on a range of your choice.

"""
from math import *
#Variables:
x1 = 1.0#This is the starting x-value
x2 = 4*atan(1)#This is the ending x-value
n = 100000#This is the number of rectangles
Area = 0.0#This is the total area
Areaf = 0.0 #This is the total area
Areag = 0.0 #This is the total area
Areah = 0.0 #This is the total area
#Functions of area calculation
def f(x):
    return sin(x)
def g(x):
    return 2**x
def h(x):
    return x*x

for i in range(1, n+1):
    for x in range(0, int(pi)):#Use a nested loop to set the range of x-values
        #Find the function value
        Aif = f(x1+(x2-x1)*i/n)*(x2-x1)/n#Find the area of the rectangle, Ai
        Areaf += Area+Aif#Add it to the total area, "Area"
    for x in range(1, 10):
        Aig = g(x1+(x2-x1)*i/n)*(x2-x1)/n
        Areag += Area+Aig
    for x in range(0, 5):
        Aih = h(x1+(x2-x1)*i/n)*(x2-x1)/n
        Areah += Area+Aih
#Print the area here
print ("x=",x,"\n(1)",Areaf,"\n(2)", Areag,"\n(3)", Areah)
    
    




