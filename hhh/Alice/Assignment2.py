#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 13:06:32 2018
Assignment2:convert numbers between strings, integers, and floats.
@author: haichunkan
"""
#Let the user enter 2 numbers(they can be integers or decimal numbers).
a=float(input("Please enter a number for a:"))
b=float(input("Please enter another numberfor b:"))
#Convert them into integers.
inta=int(a)
intb=int(b)
#Calculate them as integers, and print them.
print("a+b=",inta+intb)
print("a-b=",inta-intb)
print("a*b=",inta*intb)
print("a/b=",inta/intb)
#Calculate them as floats, and print them.
print("a+b=",a+b)
print("a-b=",a-b)
print("a*b=",a*b)
print("a/b=",a/b)
#print them as strings.
print("The sum of a and b:",str(a+b))
print("The difference of a and b:",str(a-b))
print("The product of a and b:",str(a*b))
print("The quotient for a and b:",str(a/b))