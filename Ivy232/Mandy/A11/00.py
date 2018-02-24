#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 15:11:43 2018

@author: xuwentong
"""

def Search():
        import random
        n = []
        for i in range(0,1000): # create a list of random numbers
            n.append(random.random())
            n.sort() 
        def Binary(n): # find the number which is most closest to and bigger than m,(0 < m < 1)
            mid = len(n)//2 # compare with the number in the middle to zoom in the limit
            LH = []
            RH = []
        
            if n[mid] >0.7: # then the num we want must smaller than n[mid]
                LH= n[:mid+1]
       
                if len(LH) == 2:
                    print ("Result",LH[1])
                    
                else:
                    Binary(LH)  # Recusive: keep zoom in the range
                
            elif n[mid] < 0.7: # then the num we want must larger than n[mid]
                RH = n[mid:]
            
                if len(RH) == 2:
                    print("Result",RH[1])
                
                else:
                    Binary(RH)
Search()