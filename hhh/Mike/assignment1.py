# -*- coding: utf-8 -*-
"""
Name: Xu, Yingjie (Mike)
Date: 2018-01-10
Program Title: number loop
Purpose: This program is used to print 1000 numbers from 0 to 999, and test if these numbers are divisible by 3 or 19.
Variable name: i
"""

for i in range (0,1000):
    print (i)
    if i % 3 == 0:
        print (str(i),'is divisible by 3')
    if i % 19 == 0:
        print (str(i), 'is a mutiple of 19!')
        