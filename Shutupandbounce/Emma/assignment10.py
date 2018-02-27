# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 12:19:20 2018
@author: Emma
Assignment 10 - Benchmarking Sorting Algorithms
Purpose:(1) Create a class with functions for three sorting algorithms
 - bubble sort, selection sort and insertion sort. 
(2) Write a program that determines the amount of time taken to 
    sort lists of random numbers of the following lengths: 
    n=[10000,20000,30000,40000,50000]
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
#Import source required.
import random
from timeit import timeit
from timeit import Timer
import matplotlib
import matplotlib.pyplot as plt
#create 3 sets of time taken by calculating each value in r from 3 different sorting algorithms.
a1time = []
a2time = []
a3time = []
#Create a class with functions for three sorting algorithms.
class sortingAlgorithms():
    def bubbleSort(self,r1):
        '''
        Function for bubble sort
        - makes multiple passes through a list.
        - compares adjacent items and exchanges those that are out of order. 
        '''
        #If there are n items in the list, 
        #then there are n−1 pairs of items that need to be compared on the first pass.
        print("bSort")
        for passnum in range(len(r1)-1,0,-1):
            for i in range(passnum):#Between the items for comparison:
                if r1[i] > r1[i+1]:#If the former term is greater than the letter one:
                    temp = r1[i]
                    r1[i] = r1[i+1]
                    r1[i+1] = temp#They will be swapped.
        print(r1)
        t1 = timeit.Timer('a.bSort()', 'from __main__ import a').timeit(1)
        a1time.append(t1)#time for 1 time and add them to a timeset
                                   
    def sSort(self,r1):
        '''
        Function for selection sort
        - improves on the bubble sort by making 
        only one exchange for every pass through the list. 
        - looks for the largest value as it makes a pass and, 
        after completing the pass, 
        places it in the proper location. 
        '''
        print("sSort")
        for fillslot in range(len(r1)-1,0,-1):
            positionOfMax=0
        for location in range(1,fillslot+1):
            if r1[location]>r1[positionOfMax]:
                positionOfMax = location

        temp = r1[fillslot]
        r1[fillslot] = r1[positionOfMax]
        r1[positionOfMax] = temp
        print(r1)
        t2 = timeit.Timer('a.sSort()', 'from __main__ import a').timeit(1)
        a2time.append(t2)#time for 1 time and add them to a timeset

        
    def iSort(self,r1):
        '''
        Function for insertion sort
        - always maintains a sorted sublist in 
        the lower positions of the list. 
        - Each new item is then “inserted” back 
        into the previous sublist such that the 
        sorted sublist is one item larger.
        '''
        print("iSort")
        for index in range(1,len(r1)):
            currentvalue = r1[index]
            position = index
            while position>0 and r1[position-1]>currentvalue:
                r1[position]=r1[position-1]
                position = position-1
            r1[position]=currentvalue
        print(r1)
        t3 = timeit.Timer('a.iSort()', 'from __main__ import a').timeit(1)
        a3time.append(t3)#time for 1 time and add them to a timeset
        
#create a function to display the outcome
    def output():
        for i in range(0,len(a1time)):
            print("bSort result:\n", " n      time(sec)")
            print("100"+str(a1time[i][0]))
        for j in range(0,len(a2time)):
            print("sSort result:\n", " n      time(sec)")    
            print("100"+str(a2time[j[0]]))
        for k in range(0,len(a3time)):
            print("sSort result:\n", " n      time(sec)")    
            print("100"+str(a3time[k[0]]))

#Create lists of random numbers of the lengths in "n"
r1 = []
for i in range(0,10000):
    r1.append(int(random.random()*10000))
r2 = []
for i in range(0,20000):
    r2.append(int(random.random()*20000))
r3 = []
for i in range(0,30000):
    r3.append(int(random.random()*30000))
r4 = []
for i in range(0,40000):
    r4.append(int(random.random()*40000))
r5 = []
for i in range(0,50000):
    r5.append(int(random.random()*50000))

a = sortingAlgorithms()
a.bubbleSort(r1)
a.sSort(r1)
a.iSort(r1)
timeit.Timer(a.bSort).timeit()
timeit.Timer(a.sSort).timeit()
timeit.Timer(a.iSort).timeit()
a.output()
#Make a title for the graph
plt.title("Sorting Algorithms")
#Plot the time(x-value(s),y-value(s),the style(red dots) of graph)
plt.plot(r1,[a1time,a2time,a3time],'ro:')
#Change the size of the axis label:
ax = plt.gca()
for label in ax.xaxis.get_ticklabels():
    label.set_fontsize(20)
for label in ax.yaxis.get_ticklabels():
    label.set_fontsize(20)
myfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc',size=24) 
plt.xlabel(u'functions(number)',fontproperties=myfont)#Label x-axis
plt.ylabel(u'time(sec)',fontproperties=myfont)#Label y-axis
   
