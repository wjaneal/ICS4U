# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:37:30 2018

@author: simet
"""
import random
m=random.randint(0,1001)
Answer = False
while (Answer == False):
    n=int(input('What is the number'))
    
    if m>n:
        print ('too low')
    if m<n:
        print ('too high')
    if m==n:
        print('right')
        Answer = True
        
        


