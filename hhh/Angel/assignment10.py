#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 12:55:44 2018
@author: hailankan
title:sorting algorithms
function:
(1) Create a class with functions for three sorting algorithms - bubble sort, selection sort and insertion sort. 
(2) Write a program that determines the amount of time taken to sort lists of random numbers of the following lenghs: n=[10000,20000,30000,40000,50000]
(3) Output of the program:
Bubble sort algorithm:
n	time
10000	2.23
20000	4.67
30000 	7.88
40000	11.34
50000	14.44
Insertion sort algorithm:
n	time
10000	2.23
20000	14.67
30000 	117.88
40000	211.34
50000	11214.44
Selection Sort algorithm:
n	time
10000	1.4
20000 	4.5
30000	10.4
40000	29.3
50000	100.2
(4) Have Python graph the results using pyplot / matplotlib

"""
import matplotlib.pyplot as plt
import time
import random
n=[1000,2000,3000,4000,5000]
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
#set list 12345
for i in range(0,1000):
    list1.append(int(random.random()*1000))
for i in range(0,2000):
    list2.append(int(random.random()*2000))
for i in range(0,3000):
    list3.append(int(random.random()*3000))
for i in range(0,4000):
    list4.append(int(random.random()*4000))
for i in range(0,5000):
    list5.append(int(random.random()*5000))
#put lists in a list
lists=[list1,list2,list3,list4,list5]

    

def Bubblesort():
    totalTime1=[]
    print('Bubble Sort:')
    print('n	time')
    for item in lists:#loop for each value in the n list
        start_time = time.time()
        for i in range(0,len(item)-1):
            run=True
            for j in range(0,len(item)-1-i):
                if item[j] > item[j+1]:#if left>right
                    item[j],item[j+1] = item[j+1],item[j]#exchange value
                    run=False
            if run:#if correct
                break#go to next turn
        elapsed_time = time.time() - start_time#calculate time
        totalTime1.append(elapsed_time)
        print(n[lists.index(item)], elapsed_time)        
    plt.plot(n,totalTime1)
    #add title
    plt.title('BubbleSort')
    #add x and y labels
    plt.xlabel('n')
    plt.ylabel('time')
    plt.show()#show graph
    
    
    
def Selectionsort():
    totalTime2=[]
    print('Selection Sort:')
    print('n	time')
    for item in lists:#loop for each value in the n list
        start_time = time.time()
        for i in range(len(item)-1,0,-1):#from the last element in list to first element in list
            maxIndex=0#assume the first element is the largest
            for j in range(1,i-1):#from second elemnet to the second last element
                if item[j]> item[maxIndex]:#if an element is larger than the assumed largest
                    maxIndex= j#assume the larger one is the largest
            item[i],item[maxIndex]=item[maxIndex],item[i]#exchange value between largest and last
        elapsed_time = time.time() - start_time
        totalTime2.append(elapsed_time)
        print(n[lists.index(item)], elapsed_time)
        
    plt.plot(n,totalTime2)
    #add title
    plt.title('SelectionSort')
    #add x and y labels
    plt.xlabel('n')
    plt.ylabel('time')    
    plt.show()#show graph
    
    
    
def Insertionsort():
    totalTime3=[]
    print('Insertion Sort:')
    print('n	time')
    for item in lists:#loop for each value in the n list
        start_time = time.time()
        for i in range(1,len(item)):#from second element to last element
            while i>0 and item[i-1]> item[i]:#change value with the left element if left>right 
                item[i],item[i-1]=item[i-1],item[i]
                i-=1
        elapsed_time = time.time() - start_time
        totalTime3.append(elapsed_time)
        print(n[lists.index(item)], elapsed_time)
        
    plt.plot(n,totalTime3)
    #add title
    plt.title('InsertionSort')
    #add x and y labels
    plt.xlabel('n')
    plt.ylabel('time')    
    plt.show()#show graph

Bubblesort()
Insertionsort()
Selectionsort()
     
