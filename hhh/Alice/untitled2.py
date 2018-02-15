#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 12:31:34 2018

@author: haichunkan
"""
import random
import time    
def randomR(list1):
    index=int(random.random()*12)
    while  list1.index(highest)-list1.index(lowest)!=1:
        index=int(random.random(lowest+1,highest))
        if list1[index]<num:
            lowest=list1[index]
        if list1[index]>num:
            highest=list1[index] 
    print(list1[list1.index(highest)],"is just greater than",num)        
def linear(list1):
    for i in range(0,10000):
        if list1[i]>num:
            print(list1[i],"is just greater than",num)
            break
def binary(list1):
    while  list1.index(highest)-list1.index(lowest)!=1:
        index=(list1.index(highest)+list1.index(lowest))//2
        if list1[index]<num:
            lowest=list1[index]
        if list1[index]>num:
            highest=list1[index]
    print(list1[list1.index(highest)],"is just greater than",num)   
def countTime():
    rt=[]
    lt=[]
    bt=[]
    for i in range(0,5):
        starttime=time.time()
        random(list1)
        rt.append(time.time-starttime)
        starttime=time.time()
        linear(list1)
        lt.append(time.time-starttime)
        starttime=time.time()
        binary(list1)
        bt.append(time.time-starttime)
    print(rt,lt,bt)        
        

num=int(random.random()*10000)
print("what is just greater than",num)
list1=[0,111,555,1111,2222,3333,4444,5555,6666,7777,8888,9999]
lowest=list1[0]
highest=list1[-1]
time()        