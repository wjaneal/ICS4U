# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 01:47:51 2018

@author: 11256
"""
''' 
(a)Name:Tony
(b)Date:January 11th
(c)Program title: Division
(d)Purpose: check the number is divisible by 3 and multiple of 19 in 1000 numberes.
(e)Variable name:i
'''

for i in range (0,1000):
    #loop through 1000 numbers.
    print (i)
    if i % 3 == 0:
        print (i,"divisible by 3")
        #The number is divisible by 3.
    if i %19 == 0:
        print (i,"multiple of 19")
        #The number is multiple of 19.