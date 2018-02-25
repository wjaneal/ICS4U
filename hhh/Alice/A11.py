#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 12:31:34 2018

@author: haichunkan
"""
import random
import time
import matplotlib.pyplot as plt 
   
def randomR(list1):# this is random search
    lowest=list1[0]#identify the max and min number
    highest=list1[-1]
    index=int(random.random()*12)
    while  list1.index(highest)-list1.index(lowest)!=1:
        index=int(random.uniform(list1.index(lowest)+1,list1.index(highest)))
        if list1[index]<num:
            lowest=list1[index]
        if list1[index]>num:
            highest=list1[index] #smaller the range until the difference is 1
    print(list1[list1.index(highest)],"is just greater than",num)        
def linear(list1):#linear search
    for i in range(0,len(list1)):
        if list1[i]>num:#start from beginning, until it find the number just greater 
            print(list1[i],"is just greater than",num)
            break
def binary(list1):#binary search
    lowest=list1[0]
    highest=list1[-1]
    while  list1.index(highest)-list1.index(lowest)!=1:
        index=(list1.index(highest)+list1.index(lowest))//2#make it half
        if list1[index]<num:
            lowest=list1[index]
        if list1[index]>num:
            highest=list1[index]
    print(list1[list1.index(highest)],"is just greater than",num)   
def countTime():
    list1=[]
    for i in range(0,len(n)):
        a=n[i]
        for j in range(0,int(a)):
            list1.append(j)  
        starttime=time.time()#count the time for each
        randomR(list1)
        rt.append(time.time()-starttime)
        starttime=time.time()
        linear(list1)
        lt.append(time.time()-starttime)
        starttime=time.time()
        binary(list1)
        bt.append(time.time()-starttime)       


rt=[]#store the time for each searching funtion in
lt=[]
bt=[]        
n=[100000,200000,300000,400000,500000]
for i in range(0,len(n)):
    num=int(random.random()*n[i])
    print("what is just greater than",num)
    countTime()
#Draw a graph.           
plt.plot(n, rt, color='green')#represent random search
plt.plot(n, lt, color='orange')#linear search
plt.plot(n, bt, color='blue')#binary search
#label them
plt.annotate('binary', xy=(50000,0.00001),color='blue')
plt.annotate('random', xy=(50000,0.00003),color='green')
plt.annotate('linear', xy=(50000,0.00005),color='orange')
plt.xlabel('under number n')
plt.ylabel('time needed')
plt.title('time taken by each')
plt.show()  # show the graph         