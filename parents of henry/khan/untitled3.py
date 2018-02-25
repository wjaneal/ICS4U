# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 12:54:45 2018

@author: simet
"""

L=[]
Length=int(input('tell me the length of the list'))
for m in range(0,Length):
    a=int(input('give me a number'))
def switch(one,another):
    c=one
    one=another
    another=c
Complete=True
for i in range(0,Length):
    Now = 0
    
    for j in range(Now,Length-1):
        if L[j]>L[j+1]:
            switch(L[j],L[j+1])
            Complete=False
        if Complete =True:
            print L
            
        
            