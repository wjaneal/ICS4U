#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 13:02:09 2018
@author: hailankan
Program Title: Typecast!
Purpose: convert between intergers, floating point numbers and strings
Variables:number1,number2,integer1,integer2,float1,float2,total,difference,product,quotient
"""
#Let the user input two numbers.
number1 = float(input("please input a number: "))
number2 = float(input("please input a number: "))
#Convert the numbers to integers.
integer1 = int(number1)
integer2 = int(number2)
#Print the sum, difference, product and quotient of the numbers.
print(integer1, "+", integer2, '=', integer1+integer2)
print(integer1, "-", integer2, '=', integer1-integer2)
print(integer1, "*", integer2, '=', integer1*integer2)
print(integer1, "/", integer2, '=', integer1/integer2)
##Convert the numbers to floating point.
float1 = float(number1)
float2 = float(number2)
#Print the sum, difference, product and quotient of the numbers.
print(float1, "+", float2, '=', float1+float2)
print(float1, "-", float2, '=', float1-float2)
print(float1, "*", float2, '=', float1*float2)
print(float1, "/", float2, '=', float1/float2)
# Convert the numbers to strings.
total = str(float1+float2)
difference = str(float1-float2)
product = str(float1*float2)
quotient = str(float1/float2)
#Output results.
print("The sum of "+ str(number1)+ " and "+ str(number2)+ ' is '+ total)
print("The difference of "+ str(number1)+ " and "+ str(number2)+ ' is '+ difference)
print("The product of "+ str(number1)+ " and "+ str(number2)+ ' is '+ product)
print("The quotient of "+ str(number1)+ " and "+ str(number2)+ ' is '+ quotient)