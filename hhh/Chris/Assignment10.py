# -*- coding: utf-8 -*-
"""
Assignment 10 - Benchmarking Sorting Algorithms
Coding convention: 
(a) lower case file name
(b) Name, Date, Title, Purpose in multiline comment at the beginning
(c) mixedCase variable names
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
import matplotlib.pyplot as plt


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
    def countTime(): # this is the funtion that can count time
        list1=[]
        for i in range(0,len(n)):
            for i in n:
                list1.append(i)
            random.shuffle(list1)# make a random list
            st=time.time()
            sorting.insertionSort(list1)
            eti=time.time()-st# count the time insertion sort takes
            etil.append(eti)
            st=time.time()
            sorting.selectionSort(list1)
            ets=time.time()-st# count the time seletion sort takes
            etsl.append(ets)
            st=time.time()
            sorting.bubbleSort(list1)
            etb=time.time()-st# count the time buuble sort takes
            etbl.append(etb)

n=[10000,20000,30000,40000,50000]
etil=[]
etsl=[]
etbl=[]            
sorting.countTime() # Run the program
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