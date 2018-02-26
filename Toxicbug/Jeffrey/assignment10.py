# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 13:35:50 2018

@author: Jeffrey

Purpose:

(1) Create a class with functions for three sorting algorithms - bubble sort, selection sort and insertion sort. 
(2) Write a program that determines the amount of time taken to sort lists of random numbers of the following lenghs: n=[1000,2000,3000,4000,5000]
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
#import module
import time
import matplotlib.pyplot as plt
import random 

class compareAlgorism:
    
    def bubbleSort(self): #This defines a function for Bubble sort algorithm.
        start = time.time()#This gets the start time.
        for i in range(0,len(self.alist)-1):#This loop iterates through the list to the penultimate element.
            self.swapped=False #This initializes self.swapped as False.
            for j in range(0,len(self.alist)-1-i): #This loop iterates through the unsorted part of the list.
                if self.alist[j]>self.alist[j+1]: #If the number is bigger than the next number, they need to be swapped.
                    self.alist[j],self.alist[j+1] = self.alist[j+1],self.alist[j] #This swaps the two numbers.
                    self.swapped=True #This sets self.swapped to True.
            if self.swapped==False: #If no number is swapped, the list is already sorted.
                break #This exits from the loop.
        self.bResult.append(time.time() - start)
        
    def selectionSort(self):# make a function to run selection sort 
        start = time.time()
        for i in range(len(self.alist)):
            mini = min(self.alist[i:]) #find minimum element
            min_index = self.alist[i:].index(mini) #find index of minimum element
            self.alist[i + min_index] = self.alist[i] #replace element at min_index with first element
            self.alist[i] = mini#replace first element with min element
        self.sResult.append(time.time() - start)
        
    def insertionSort(self): # make a function to run insertion sort
        start = time.time()
        #iterating over alist
        for i in self.alist:
            j = self.alist.index(i)
            #i is not the first element
            while j>0:
                #not in order
                if self.alist[j-1] > self.alist[j]:
                    #swap
                    self.alist[j-1],self.alist[j] = self.alist[j],self.alist[j-1]
                else:
                    #in order
                    break
                    j = j-1
        self.iResult.append(time.time() - start)
    def generateLists(self):
        self.testLists = [] # create a 2D list restoring sets of numbers
        for a in range(0,5):
            self.testLists.append([])
        n = [1000,2000,3000,4000,5000] # The lenghs of lists
        # major loop that iterate five numbers of n
        for i in range(0,len(n)):
            #subloop that append randam numbers to each set
            for ii in range(0, n[i]):
                self.testLists[i].append(random.randint(0,100000))
            i += 1 # make sure it iterate one after another
        
    def benchMarking(self):
        n = [1000,2000,3000,4000,5000] # The lenghs of lists
        self.bResult = []#creat a list that restore the result 
        self.sResult = []#creat a list that restore the result 
        self.iResult = []#creat a list that restore the result 
        self.generateLists()
        for i in range(0, 5):
            self.alist = self.testLists[i]
            self.bubbleSort()

        for ii in range(0, 5):
            self.alist = self.testLists[ii]
            self.selectionSort()
            #self.sResult.append(self.period)
        for iii in range(0, 5):
            self.alist = self.testLists[iii]
            self.insertionSort()
            #self.iResult.append(self.period)
        # print results lists
        print("\nBubble sort algorithm:")
        print("n    time")
        for b in range(0, 5):
            print(n[b], self.bResult[b])
        plt.plot(n, self.bResult) #plot a graph for results for bubble sort
        plt.ylabel('Times take for Bubble Sort')
        plt.xlabel('number')
        plt.show() #show the results
        print("\nSelection sort algorithm:")
        print("n    time")
        for s in range(0, 5):
            print(n[s], self.sResult[s])
        plt.plot(n ,self.sResult) #plot a graph for results for selection sort
        plt.ylabel('Times take for Selection Sort')
        plt.xlabel('number')
        plt.show() #show the results
        print("\nInsertion sort algorithm:")
        print("n    time")
        for I in range(0, 5):
            print(n[I], self.iResult[I])
        plt.plot(n ,self.iResult) #plot a graph for results for insertion sort
        plt.ylabel('Times take for Insertion Sort')
        plt.xlabel('number')
        plt.show() #show the results
a = compareAlgorism()
a.benchMarking()


































































