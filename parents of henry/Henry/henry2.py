# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Name:Henry
Date: 11/Tan/2018
Program Title: Type casting
Purpose:(
(a) Let the user input two numbers.
(b) Convert the numbers to integers
(c) Print the sum, difference, product and quotient of the numbers.
(d) Repeat (b) and (c) for floating point
(e) Convert the numbers to strings.
(f) Output the four results as strings as follows: The sum of a and b is 5.667, etc. for subtraction, multiplication and division.

    
""" 
a = eval(input ('give me a number:'))
b = eval(input ('give me another number:'))
int1 = int(a)
int2 = int(b)
print('------------------ integers')
print('the sum is',int1+int2)
print('the difference is',int1-int2)
print('the product is',int1*int2)
print('the quotient is',int1/int2)

f1 = float(a)
f2 = float(b)
print('------------------ floats')
print('the sum is',f1+f2)
print('the difference is',f1-f2)
print('the product is',f1*f2)
print('the quotient is',f1/f2)
print('------------------')
print('the sum of ' + str(a) + ' and ' + str(b) + ' is  ' +str(f1+f2))
print('the difference of ' + str(a) + ' and ' + str(b) + ' is ' +str(f1-f2))
print('the product of ' + str(a) + ' and ' + str(b) + ' is ' +str(f1*f2))
print('the quotient of ' + str(a) + ' and ' + str(b) + ' is ' +str(f1/f2))
    
    
    
    
    

    