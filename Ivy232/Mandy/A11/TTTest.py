#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:57:16 2018

@author: Mandy
"""
import random
n = []
for i in range(0,1000):
    n.append(random.random())
    n.sort()
def Binary(n):
        
    mid = len(n)//2
    LH = []
    RH = []
        
    if n[mid] > 0.7:
        LH = n[:mid+1]
        #print("LH",LH)
        #print("1",LH)
        if len(LH) == 2:
            #print(LH)
            print ("Result",LH[1])
            pass
        else:
            Binary(LH)  
            #print("3",LH)
    elif n[mid] < 0.7:
        RH = n[mid:]
        #print(RH)
        #print("4",RH)
        if len(RH) == 2:
            #print("RH",RH)
            print("Result",RH[1])
            pass
        else:
            Binary(RH)
            #print("6",RH)
    


#print("n",n)
Binary(n)
