#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Charlotte Chen
Date: Created on Mon Feb 12, 2018
Title: Benchmarking Sorting Algorithms
Purpose: 
(1) Create a class with functions for three sorting algorithms - bubble sort, selection sort and insertion sort. 
(2) Write a program that determines the amount of time taken to sort lists of random numbers of the following lenghs: n=[10000,20000,30000,40000,50000]
(3) Print the time and corresponding n value for each sorting algorithm.
(4) Have Python graph the results using pyplot / matplotlib
"""
import time 
import random
import matplotlib.pyplot as plt

#integerRange=[10000,20000,30000,40000,50000]
integerRange=[1000,2000,3000,4000,5000] #This defines the length of the list of random numbers.
timeB=[] #This creates an empty list to store n values and time for the Bubble sort algorithm.
timeS=[] #This creates an empty list to store n values and time for the Selection sort algorithm.
timeI=[] #This creates an empty list to store n values and time for the Insertion sort algorithm.

class sorting: #This creates a class for three sorting algorithms.
    def bubbleSort(self,list1,n): #This defines a function for Bubble sort algorithm.
        startTime=time.time()#This gets the start time.
        for i in range(0,len(list1)-1):#This loop iterates through the list to the penultimate element.
            self.swapped=False #This initializes self.swapped as False.
            for j in range(0,len(list1)-1-i): #This loop iterates through the unsorted part of the list.
                if list1[j]>list1[j+1]: #If the number is bigger than the next number, they need to be swapped.
                    list1[j],list1[j+1] = list1[j+1],list1[j] #This swaps the two numbers.
                    self.swapped=True #This sets self.swapped to True.
            if self.swapped==False: #If no number is swapped, the list is already sorted.
                break #This exits from the loop.
        timeB.append((n,time.time()-startTime)) #This appends the n value and the execution time to a list.

    def selectionSort(self,list1,n): #This defines a function for Selection sort algorithm.
        startTime=time.time() #This gets the start time.
        for i in range(0,len(list1)-1): #This loop iterates through the list to the penultimate element.
            minIndex=i #This sets the minimum of the list to the number with the index i.
            for j in range(i+1,len(list1)): #This loop iterates through the list, starting from the number with index (i+1).
                if list1[j]<list1[minIndex]: #If the number is smalled than the minimum set before, its index is set to the index of minimum.
                    minIndex=j
            if minIndex!=i: #If the index of the minimum changes, the two numbers should be swapped.
                list1[i],list1[minIndex] = list1[minIndex],list1[i] #This swaps the two numbers.
        timeS.append((n,time.time()-startTime)) #This appends the n value and the execution time to a list.

    def insertionSort(self,list1,n): #This defines a function for Insertion sort algorithm.
        startTime=time.time() #This gets the start time.
        for i in range(1,len(list1)): #This loop iterates through the list,starting from the second element.
            curNum=list1[i] #This initializes curNum as the element in the list with index i.
            for j in range(i-1,-1,-1): #This loop iterates through the prior numbers of the element with index i.
                if list1[j]>curNum: #If the number is larger than the number with index i, its value is set to the next element in the list.
                    list1[j+1]=list1[j]
                else:
                    list1[j+1]=curNum #If the number is not larger than the number with index i, nothing happens.
                    break #This exits from the inner loop and proceeds to the next element.
            if list1[0]>curNum: #If the first element in the list is bigger than the current number tested, the value of the current number is set to the first element.
                list1[0]=curNum
        timeI.append((n,time.time()-startTime)) #This appends the n value and the execution time to a list.

a=sorting() #This creates an instance of the sorting class.
list1=[] #This creates an empty list to store the numbers.
for i in integerRange: #This loop iterates through all the integer ranges
    for j in range(0,i): #This loop appends a certain number of random numbers to the list.
        list1.append(int(random.random()*(i+1)))
    a.bubbleSort(list1,i) #This uses the Bubble sort algorithm to sort the numbers.
    a.insertionSort(list1,i) #This uses the Insertion sort algorithm to sort the numbers.
    a.selectionSort(list1,i) #This uses the Selection sort algorithm to sort the numbers.
    
print("Bubble sort algorithm:")#This prints the n values and corresponding execution time for the Bubble sort algorithm.
print("n"+"         "+"time")
for i in range(0,len(timeB)):
    print(str(timeB[i][0])+"     "+str(timeB[i][1]))
print("Insertion sort algorithm:")#This prints the n values and corresponding execution time for the Insertion sort algorithm.
print("n"+"         "+"time")
for i in range(0,len(timeI)):
    print(str(timeI[i][0])+"     "+str(timeI[i][1]))
print("Selection sort algorithm:") #This prints the n values and corresponding execution time for the Selection sort algorithm.
print("n"+"         "+"time")
for i in range(0,len(timeS)):
    print(str(timeS[i][0])+"     "+str(timeS[i][1]))
time1=[] #This creates an empty list for storing the y values for the Bubble sort algorithm.
time2=[] #This creates an empty list for storing the y values for the Insertion sort algorithm.
time3=[] #This creates an empty list for storing the y values for the Selection sort algorithm.
for i in timeB:
    time1.append(i[1]) #This appends the time of the Bubble sort algorithm to the list.
time2=[]
for i in timeI:
    time2.append(i[1]) #This appends the time of the Insertion sort algorithm to the list.
time3=[]
for i in timeS:
    time3.append(i[1]) #This appends the time of the Selection sort algorithm to the list.
plt.plot(integerRange, time1,color='red') #This generates the graph for the Bubble sort algorithm.
plt.plot(integerRange,time2,color='blue') #This generates the graph for the Insertion sort algorithm.
plt.plot(integerRange,time3,color='green') #This generates the graph for the Selection sort algorithm.
plt.title('Benchmarking Sorting Algorithms') #This creates a title for the graph.
plt.ylabel('Time') #This creates the y label for the graph.
plt.xlabel('n Value') #This creates the x label for the graph.
plt.show()

