#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: chenquancheng
Date: Created on Thu Jan 11 12:46:32 2018
Title: typecasting
Purpose: lets the user input two numbers, typecasts them to different data types and does some calculations 
"""
x=input("Please input a number") #lets the user input two numbers
y=input("Please input another number")
xInteger=int(x)#converts numbers to integers
yInteger=int(y)
#integer calculations
intSum=xInteger+yInteger
intDifference=abs(xInteger-yInteger) #uses the absolute value to get the positive difference
intProduct=xInteger*yInteger
intQuotient=int(xInteger/yInteger) #I have to typecast the quotient to an integer because python3 automatically calculates the division of two integers as floating point numbers
#print integer sum, difference, product,and quotient.
print(intSum)
print(intDifference)
print(intProduct)
print(intQuotient)
xFloat=float(x)#converts numbers to floating point numbers
yFloat=float(y)
#floating point number calculations
floatSum=xFloat+yFloat
floatDifference=abs(xFloat-yFloat)
floatProduct=xFloat*yFloat
floatQuotient=xFloat/yFloat
#print floating point sum, difference, product, and quotient
print(floatSum)
print(floatDifference)
print(floatProduct)
print(floatQuotient)  
#converts numbers to strings
stringSum=str(floatSum)
stringDifference=str(floatDifference)
stringProduct=str(floatProduct)
stringQuotient=str(floatQuotient)
#print string sum, difference, product, and quotient
print("The sum of x and y is "+stringSum)
print("The difference of x and y is "+stringDifference)
print("The product of x and y is "+stringProduct)
print("The quotient of x and y is "+stringQuotient)