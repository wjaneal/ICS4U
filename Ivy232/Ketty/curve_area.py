#Name: Ketty
#Date: January 15, 2018
#Program Title: Area Calculator
#Program Function: This program calcuates the area under curves (mathematical functions)
from math import *
#Variables:
a = 1.0 #This is the starting x value
b = 5.0 #This is the ending x value
n = 1000000 #This is the number of rectangles
Area = 0.0 #This is the total area

#This is the function to use in the area calculation
def f(x):
    return x*x

def g(x):
    return sin(x)

def h(x):
    return 2**x

for i in range(1,n+1):
    #Find xi, the current x value
    xi = (b-a)/n
    #Find the area of the rectangle, Ai, using the function
    Ai = f(a+i*xi)*((b-a)/n)
    #Add it to the total area, "Area"
    Area += Ai
#Print the area here
print (Area)

a = 0
b = pi
AreaII = 0.0

for i in range(1,n+1):
    #Find xi, the current x value
    xiII = (b-a)/n
    #Find the area of the rectangle, Ai, using the function
    AiII = g(a+i*xiII)*((b-a)/n)
    #Add it to the total area, "Area"
    AreaII += AiII
#Print the area here
print (AreaII)


a = 1
b = 10
AreaIII = 0.0

for i in range(1,n+1):
    #Find xi, the current x value
    xiIII = (b-a)/n + a
    #Find the area of the rectangle, Ai, using the function
    AiIII = h(a+i*((b-a)/n))*((b-a)/n)
    #Add it to the total area, "Area"
    AreaIII += AiIII
#Print the area here
print (AreaIII)
