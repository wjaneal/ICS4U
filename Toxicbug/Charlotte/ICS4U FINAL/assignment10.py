#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Charlotte Chen
Date: Created on Mon Feb 12, 2018
Title: Benchmarking Sorting Algorithms
Purpose: 
(1) Create a class with functions for three sorting algorithms - bubble sort, selection sort and insertion sort. 
(2) Write a program that determines the amount of time taken to sort lists of random numbers of the following lenghs: n=[1000,2000,3000,4000,5000]
(3) Print the time and corresponding n value for each sorting algorithm.
(4) Have Python graph the results using pyplot / matplotlib
"""
import time 
import random
import matplotlib.pyplot as plt

class sorting: #This creates a class for three sorting algorithms.
    def bubbleSort(self): #This defines a function for Bubble sort algorithm.
        startTime=time.time()#This gets the start time.
        for i in range(0,len(self.list1)-1):#This loop iterates through the list to the penultimate element.
            self.swapped=False #This initializes self.swapped as False.
            for j in range(0,len(self.list1)-1-i): #This loop iterates through the unsorted part of the list.
                if self.list1[j]>self.list1[j+1]: #If the number is bigger than the next number, they need to be swapped.
                    self.list1[j],self.list1[j+1] = self.list1[j+1],self.list1[j] #This swaps the two numbers.
                    self.swapped=True #This sets self.swapped to True.
            if self.swapped==False: #If no number is swapped, the list is already sorted.
                break #This exits from the loop.
        self.timeB.append((self.n,time.time()-startTime)) #This appends the n value and the execution time to a list.

    def selectionSort(self): #This defines a function for Selection sort algorithm.
        startTime=time.time() #This gets the start time.
        for i in range(0,len(self.list1)-1): #This loop iterates through the list to the penultimate element.
            minIndex=i #This sets the minimum of the list to the number with the index i.
            for j in range(i+1,len(self.list1)): #This loop iterates through the list, starting from the number with index (i+1).
                if self.list1[j]<self.list1[minIndex]: #If the number is smalled than the minimum set before, its index is set to the index of minimum.
                    minIndex=j 
            if minIndex!=i: #If the index of the minimum changes, the two numbers should be swapped.
                self.list1[i],self.list1[minIndex] = self.list1[minIndex],self.list1[i] #This swaps the two numbers.
        self.timeS.append((self.n,time.time()-startTime)) #This appends the n value and the execution time to a list.

    def insertionSort(self): #This defines a function for Insertion sort algorithm.
        startTime=time.time() #This gets the start time.
        for i in range(1,len(self.list1)): #This loop iterates through the list,starting from the second element.
            curNum=self.list1[i] #This initializes curNum as the element in the list with index i.
            for j in range(i-1,-1,-1): #This loop iterates through the prior numbers of the element with index i.
                if self.list1[j]>curNum: #If the number is larger than the number with index i, its value is set to the next element in the list.
                    self.list1[j+1]=self.list1[j]
                else:
                    self.list1[j+1]=curNum #If the number is not larger than the number with index i, nothing happens.
                    break #This exits from the inner loop and proceeds to the next element.
            if self.list1[0]>curNum: #If the first element in the list is bigger than the current number tested, the value of the current number is set to the first element.
                self.list1[0]=curNum
        self.timeI.append((self.n,time.time()-startTime)) #This appends the n value and the execution time to a list.
    
    def benchmarking(self):
        self.integerRange=[10000] #This defines the length of the list of random numbers.
        self.timeB=[] #This creates an empty list to store n values and time for the Bubble sort algorithm.
        self.timeS=[] #This creates an empty list to store n values and time for the Selection sort algorithm.
        self.timeI=[] #This creates an empty list to store n values and time for the Insertion sort algorithm.
        for i in self.integerRange: #This loop iterates through all the integer ranges
            self.list1=[] #This creates an empty list to store the numbers.
            for j in range(0,i-2): #This loop appends a certain number of random numbers to the list.
                self.list1.append(int(random.random()*(i+1)))
            self.list1.sort()
            self.list1.append(9)
            self.list1.append(1)
            self.n=i
            a.bubbleSort() #This uses the Bubble sort algorithm to sort the numbers.
            a.insertionSort() #This uses the Insertion sort algorithm to sort the numbers.
            a.selectionSort() #This uses the Selection sort algorithm to sort the numbers.    
        print("Bubble sort algorithm:")#This prints the n values and corresponding execution time for the Bubble sort algorithm.
        print("n"+"         "+"time")
        for i in range(0,len(self.timeB)):
            print(str(self.timeB[i][0])+"     "+str(self.timeB[i][1]))
        print("Insertion sort algorithm:")#This prints the n values and corresponding execution time for the Insertion sort algorithm.
        print("n"+"         "+"time")
        for i in range(0,len(self.timeI)):
            print(str(self.timeI[i][0])+"     "+str(self.timeI[i][1]))
        print("Selection sort algorithm:") #This prints the n values and corresponding execution time for the Selection sort algorithm.
        print("n"+"         "+"time")
        for i in range(0,len(self.timeS)):
            print(str(self.timeS[i][0])+"     "+str(self.timeS[i][1]))
        self.graphing()
    
    def graphing(self):
        self.time1=[] #This creates an empty list for storing the y values for the Bubble sort algorithm.
        self.time2=[] #This creates an empty list for storing the y values for the Insertion sort algorithm.
        self.time3=[] #This creates an empty list for storing the y values for the Selection sort algorithm.
        for i in self.timeB:
            self.time1.append(i[1]) #This appends the time of the Bubble sort algorithm to the list.
        for i in self.timeI:
            self.time2.append(i[1]) #This appends the time of the Insertion sort algorithm to the list.
        for i in self.timeS:
            self.time3.append(i[1]) #This appends the time of the Selection sort algorithm to the list.
        plt.plot(self.integerRange,self.time1,color='red') #This generates the graph for the Bubble sort algorithm.
        plt.plot(self.integerRange,self.time2,color='blue') #This generates the graph for the Insertion sort algorithm.
        plt.plot(self.integerRange,self.time3,color='green') #This generates the graph for the Selection sort algorithm.
        plt.title('Benchmarking Sorting Algorithms') #This creates a title for the graph.
        plt.ylabel('Time') #This creates the y label for the graph.
        plt.xlabel('n Value') #This creates the x label for the graph.
        plt.show()

a=sorting() #This creates an instance of the sorting class.
a.benchmarking() #This starts the program.
    


