#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
(a)Name: chenquancheng
(b)Date: Created on Wed Jan 10 12:41:32 2018
(c)Program Title: division
(d)Purpose: loops through 1000 numbers and determines whether they are divisible by 3 and 19
"""
for i in range(0,1000): #This makes the program loop through 1000 numbers.
    if i%3==0: #If the number is divisible by 3,
        print("divisible by 3") #print "divisible by 3"
    if i%19==0: #If the number is divisible by 19,
        print("Multiple of 19!") #print "Multiple of 19!"
