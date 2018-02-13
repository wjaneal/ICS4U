#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 13:03:32 2018

@author:Mandy

Assignment 10 - Benchmarking Sorting Algorithms

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
import random
import time


class sorting():
    a1times = []
    a2times = []
    a3times = []
    def bubbleSort(list):
        n = len(list)
        # Push the largest num to the end.
        for i in range (0,n-1): # (n-1) is the biggest num of times to sort.
            for j in range (0,n-1-i): # (n-1-i) is the largest num of times that you need to swap in each i.
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1], list[j]
        return(list) # from the small num to the large num.
        #del n
    def selectionSort(alist):
        for fillslot in range(len(alist)-1,0,-1):
            positionOfMax=0
            for location in range(1,fillslot+1):
                if alist[location]>alist[positionOfMax]:
                    positionOfMax = location
            temp = alist[fillslot]
            alist[fillslot] = alist[positionOfMax]
            alist[positionOfMax] = temp
        return(alist)
        
    def insertionSort(l):
        for index in range(1,len(l)):
            currentvalue = l[index]
            position = index
            
            while position>0 and l[position-1]>currentvalue:
                l[position]=l[position-1]
                position = position-1
            
            l[position]=currentvalue
        return(l)
    
    n=[1000,2000,3000,4000,5000]
    ############################
    # print diagrams
    print("Bubble Sort Algorithm")
    print("n","         ","time")
    for z in range(0, len(n)):
        for num in n:
            list = random.sample(range(num), 10)
            t0 = time.time()
            bubbleSort(list)
            t1 = time.time()
            total = t1-t0
        a1times.append(total)
        print(n[z],"    ",total)
    print("               ")
    ############################

    print("Selection Sort Algorithm")
    print("n","         ","time")
    for z in range(0, len(n)):
        for num in n:
            list = random.sample(range(num), 10)
            t0 = time.time()
            selectionSort(list)
            t1 = time.time()
            total = t1-t0
        a2times.append(total)
        print(n[z],"    ",total)
    print("               ")
    ############################ 
    
    print("Insertion Sort algorithm")
    print("n","         ","time")
    for z in range(0, len(n)):
        for num in n:
            list = random.sample(range(num), 10)
            t0 = time.time()
            insertionSort(list)
            t1 = time.time()
            total = t1-t0
        a3times.append(total)
        print(n[z],"    ",total)
    print("               ")
############################
    import pylab as pl
    #draw diagrams


    #diagram1
    pl.plot(n, a1times)# use pylab to plot x and y: pl.plot（x，y）x and y is two lists
    pl.show()# show the plot on the screen

    #diagram2
    pl.plot(n, a2times)
    pl.show()

    #diagram3
    pl.plot(n, a3times)
    pl.show()