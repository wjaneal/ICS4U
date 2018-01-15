#Name:Khan
#Date: January 15, 2018
#Program Title: Area Calculator
#Program Function: This program calcuates the area under curves (mathematical functions)

import math
#Variables:

n = int(1000000) #This is the number of rectangles
Area = 0.0 #This is the total area

#This is the function to use in the area calculation
def f(x):
    return math.sin(x)

a = 0.0 #This is the starting x value
b = math.pi #This is the ending x value
for i in range(1,n+1):
    #Find xi, the current x value
    xi =  float(1+(i-1)*(b-a)/n)
    #Find the area of the rectangle, Ai, using the function
    Ai = float(((b-a)/n))*float(f(xi))#i made some change here
    #Add it to the total area, "Area"
    Area += Ai
#Print the area here
print (Area)

Area=0.0
a = 1.0 #This is the starting x value
b = 10.0 #This is the ending x value

def g(x):
    return x*x


for i in range(1,n+1):
    #Find xi, the current x value
    xi =  float(1+(i-1)*(b-a)/n)
    #Find the area of the rectangle, Ai, using the function
    Ai = float(((b-a)/n))*float((g(xi+(b-a)/n)+g(xi))/2)#i made some change here
    #Add it to the total area, "Area"
    Area += Ai
#Print the area here
print (Area)

Area=0.0
a = 1.0 #This is the starting x value
b = 2.0 #This is the ending x value

def h(x):
    return x


for i in range(1,n+1):
    #Find xi, the current x value
    xi =  float(1+(i-1)*(b-a)/n)
    #Find the area of the rectangle, Ai, using the function
    Ai = float(((b-a)/n))*float((h(xi+(b-a)/n)+h(xi))/2)#i made some change here
    #Add it to the total area, "Area"
    Area += Ai
#Print the area here
print (Area)



