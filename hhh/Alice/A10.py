#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 13:45:55 2018
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
@author: haichunkan
"""
import random
import time
import matplotlib.pyplot as plt
class SortingFuntion():
    def bubbleSort(list1):# Define buuble sort funtion.
        exchanges = True
        passnum = len(list1)-1# this shows how many number has passes
        while passnum > 0 and exchanges:
            exchanges = False
            for i in range(passnum):
                if list1[i]>list1[i+1]:
                    exchanges = True
                    temp = list1[i]
                    list1[i] = list1[i+1]
                    list1[i+1] = temp#change places
                passnum = passnum-1
       
    def selectionSort(list1):# Define seletion sort funtion
        for fillslot in range(len(list1)-1,0,-1):
           positionOfMax=0
           for location in range(1,fillslot+1):
               if list1[location]>list1[positionOfMax]:
                   positionOfMax = location
                   temp = list1[fillslot]
                   list1[fillslot] = list1[positionOfMax]
                   list1[positionOfMax] = temp#change places
    def insertionSort(list1):# Define insertion sort funtion
        for i in range(1,len(list1)):

            currentvalue = list1[i]

            while i>0 and list1[i-1]>currentvalue:
                list1[i]=list1[i-1]
                i = i-1
            list1[i]=currentvalue#exchange their value
    def countTime(): # this is the funtion that can count time
        list1=[]
        for i in range(0,len(n)):
            for i in n:
                list1.append(i)
            random.shuffle(list1)# make a random list
            st=time.time()
            SortingFuntion.insertionSort(list1)
            eti=time.time()-st# count the time insertion sort takes
            etil.append(eti)
            st=time.time()
            SortingFuntion.selectionSort(list1)
            ets=time.time()-st# count the time seletion sort takes
            etsl.append(ets)
            st=time.time()
            SortingFuntion.bubbleSort(list1)
            etb=time.time()-st# count the time buuble sort takes
            etbl.append(etb)

n=[10000,20000,30000,40000,50000]
etil=[]
etsl=[]
etbl=[]            
SortingFuntion.countTime() # Run the program
#Draw a graph.           
plt.plot(n, etil, color='green')#represent insertion sort
plt.plot(n, etsl, color='orange')#selection sort
plt.plot(n, etbl, color='blue')#bubble sort
#label them
plt.annotate('bubble sort', xy=(50000,0.00001),color='blue')
plt.annotate('insertion sort', xy=(50000,0.00003),color='green')
plt.annotate('bubble sort', xy=(50000,0.00005),color='orange')
plt.xlabel('under number n')
plt.ylabel('time needed')
plt.title('time taken by each sorting funtion')
plt.show()  # show the graph          
    
       
