# -*- coding: utf-8 -*-
"""
Name: Song, Jiwei (Mark)
Date: 2018-01-10
Program Title: Division
Purpose: The purpose is to loop numbers from 1 to 999, and test whether the numbers could be divisble by 3 or 19.
Variable name: i
"""

for i in range (0,1000):
    print (i)
    if i % 3 == 0:
        print(str(i),"is divisible by 3")
    if i % 19 == 0:
        print(str(i),"is a multiple of 19!")
        
        
        