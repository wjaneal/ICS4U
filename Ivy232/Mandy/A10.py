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
   

    def bubbleSort(self):
        n = len(list)
        # Push the largest num to the end.
        for i in range (0,n-1): # (n-1) is the biggest num of times to sort.
            for j in range (0,n-1-i): # (n-1-i) is the largest num of times that you need to swap in each i.
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1], list[j]
        return(list) # from the small num to the large num.
        #del n
    
    def selectionSort(self):
        for fillslot in range(len(list)-1,0,-1):
            positionOfMax=0
            for location in range(1,fillslot+1):
                if list[location] > list[positionOfMax]:
                    positionOfMax = location
            temp = list[fillslot]
            list[fillslot] = list[positionOfMax]
            list[positionOfMax] = temp
        return(list)
        
    def insertionSort(self):
        for index in range(1,len(list)):
            currentvalue = list[index]
            position = index
            
            while position>0 and list[position-1]>currentvalue:
                list[position]=list[position-1]
                position = position-1
            
            list[position]=currentvalue
        return(list)
    
    
    ############################
    
a = sorting()




a1times = []
a2times = []
a3times = []
n=[1000,2000,3000,4000,5000]
k = [100,200,300,400,500]
for z in range(0, len(n)): # pick k (size) from n (range)
    for num in n:
        list = random.sample(range(num), k[z])
        t0 = time.time()  
        a.bubbleSort()  
        t1 = time.time()
        total = t1-t0  # timing the speed of each function
    
            
        tA = time.time()
        a.selectionSort()
        tB = time.time()
        totalC = tB-tA # timing the speed of each function
   
            
        ti = time.time()
        a.insertionSort()
        tii = time.time()
        totaliii = tii-ti # timing the speed of each function
        
    a1times.append(total) # record the time used in each test
    a2times.append(totalC)
    a3times.append(totaliii)
# print forms
print("Bubble Sort Algorithm")
print("n","         ","time")
for i in range (0,5):
    print(n[i],"    ",a1times[i])
print("               ")

print("Selection Sort Algorithm")
print("n","         ","time")
for i in range (0,5):
    print(n[i],"    ",a2times[i])
print("               ")

print("Insertion Sort algorithm")
for i in range (0,5):
    print(n[i],"    ",a3times[i])
##########################
import matplotlib.pyplot as plt
#draw diagrams

plt.plot(n,a1times,color='red') # Bubble sort algorithm
plt.plot(n,a2times,color='blue') # Selection sort algorithm
plt.plot(n,a3times,color='green') # Insertion sort algorithm
plt.title('Benchmarking Sorting Algorithms') # title ofthe graph
plt.ylabel('Time') # y label for the graph
plt.xlabel('n Value') # x label for the graph
plt.show()

