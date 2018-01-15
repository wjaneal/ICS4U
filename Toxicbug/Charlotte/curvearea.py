'''
Name: Charlotte Chen
Date: January 15, 2018
Program Title: Area Calculator
Program Function: This program calcuates the area under curves (mathematical functions)
'''
from math import *
#Variables:
a = 1.0 #This is the starting x value
b = 5.0 #This is the ending x value
n = 1000000 #This is the number of rectangles
Area = 0.0 #This is the total area
#This is the function to use in the area calculation
def f(x):
    return x*x

def f1(x):
    return sin(x)

def f2(x):
    return 2**x

def f3(x):
    return (3*x+4)

for i in range(1,n+1):
    #Find xi, the current x value
    xi = a+((b-a)/n)*i
    #Find the area of the rectangle, Ai, using the function
    Ai = f(xi)*(b-a)/n
    #Add it to the total area, "Area"
    Area += Ai
#Print the area here
print(Area)

#(1) Find the area under y = sin(x) from x=0 to x = PI.
a = 1.0
b = 4*atan(1)
Area = 0.0
for i in range(1,n+1):
    #Find xi, the current x value
    xi = a+((b-a)/n)*i
    #Find the area of the rectangle, Ai, using the function
    Ai = f1(xi)*(b-a)/n
    #Add it to the total area, "Area"
    Area += Ai
#Print the area here
print(Area)

#(2) Find the area under y = 2^x from x = 1 to x = 10

a = 1.0
b = 10.0
Area = 0.0
for i in range(1,n+1):
    #Find xi, the current x value
    xi = a+((b-a)/n)*i
    #Find the area of the rectangle, Ai, using the function
    Ai = f2(xi)*(b-a)/n
    #Add it to the total area, "Area"
    Area += Ai
#Print the area here
print(Area)
#(3) Find the area under y = 3x+4 from x = 1 to x = 5
a = 1.0
b = 5.0
Area = 0.0
for i in range(1,n+1):
    #Find xi, the current x value
    xi = a+((b-a)/n)*i
    #Find the area of the rectangle, Ai, using the function
    Ai = f3(xi)*(b-a)/n
    #Add it to the total area, "Area"
    Area += Ai
#Print the area here
print(Area)


