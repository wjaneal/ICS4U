# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 19:16:04 2018
@author: fy
Assignment 11 - Linear, Random and Binary Searching - Benchmarking
Purpose:


(3) Sample output of the program:
Random search algorithm:   Linear Search Algorithm:   Binary Search algorithm:
trial#	time               trial#	time              trial#	time
1	2.23                   1	3.45                  1	    0.56
2	2.67                   2	3.97                  2 	0.87
3 	2.88                   3 	3.21                  3	    0.23
4   2.92                   4	1.23                  4	    0.34
5	2.11                   5	2.23                  5	    0.12
Average: 2.56              Average ...                Average ....
"""
#Import source required.
import random 
import matplotlib
import matplotlib.pyplot as plt
#(1) Create a class with functions for three search algorithms - random, linear and binary. 
class search():
def linearSearch(list1,tv):#tv=target value
    '''
    This method takes a list and a target value as parameters,
    which returns the index of the target value.
    If the target value is not found, the method returns '-1'.
    '''
    #Inclusive:Exclusive
    for i in range(0,len(list1)):
        #print(list1[i])
        if list1[i] == tv:
            #print("Found",tv," at index",i)
            return i#Function stops.
    return -1#Display '-1' for no results being given.
    
def binarySearch(list1,tv):
    '''
    This method allows you to search an ordered list of elements 
    very efficiently using a divide-and-conquer strategy.
    If the target value is not found, the method returns False.
    '''
    #Iterative
    found = False
    low = 0#2 vaviables declared: the first index of element;
    high = len(list1) - 1#The index of last element in list - 1.
    while low <= high and not found:#Starting 
        mid=(low + high)//2#This determines the index of the middle one.
        if tv == list1[mid]:#If the target value is the middle element of the list:
            found = True#The element is found.
        #Shift where high point is:
        elif tv < list1[mid]:#If the target value is less than the middle one:
            high=mid-1#Cut all the elements which are behind the middle out.
        #or shift where the low point is:
        else:
            low=mid+1#Cut all the elements which are in front of the middle out.
    return found  

def randomSearch(list1,tv):
    for i in list1:
        if tv in list1:
            return True
        else:
            return False
                
#Insert 10 random numbers in the list, ranging from 0 to 1000000.            
list1 = []
for i in range(0,1000000):
    list1.append(int(random.random()*1000000))
#print(list1)

r = search()

r.linearSearch(list1,1)
r.linearSearch(list1,2)
r.linearSearch(list1,3)
r.linearSearch(list1,4)
r.linearSearch(list1,5)
#loc = r.linearSearch(list1,11)
#print(loc)

r.binarySearch(list1,1)
r.binarySearch(list1,2)
r.binarySearch(list1,3)
r.binarySearch(list1,4)
r.binarySearch(list1,5)
#loc = r.binarySearch(list1,1)

print(list1)
if loc:
    print("in")
else:
    print("NONE")

r.randomSearch(list1,1)
r.randomSearch(list1,2)
r.randomSearch(list1,3)
r.randomSearch(list1,4)
r.randomSearch(list1,5)


linearSearch(list1,1)
binarySearch(list1,1)
randomSearch(list1,1)
linearSearch(list1,2)
binarySearch(list1,2)
randomSearch(list1,2)
linearSearch(list1,3)
binarySearch(list1,3)
randomSearch(list1,3)
linearSearch(list1,4)
binarySearch(list1,4)
randomSearch(list1,4)
linearSearch(list1,5)
binarySearch(list1,5)
randomSearch(list1,5)
    
    
#(2) Write a program that determines the amount of time taken to search lists of 1000000 random numbers.
if __name__=='__main__':
    from timeit import Timer
    t1=Timer("linearSearch(list1,tv)","from __main__ import linearSearch")
    t2=Timer("binarySearch(list1,tv)","from __main__ import binarySearch")
    t3=Timer("randomSearch(list1,tv)","from __main__ import randomSearch")
    print(t1.timeit(1000000))
    print(t2.timeit(1000000))
    print(t3.timeit(1000000))

#Make a title for the graph
plt.title("Sorting Algorithms")
#Plot the time(x-value(s),y-value(s),the style(red dots) of graph)
plt.plot(t1,t2,t3,'ro:')
#Change the size of the axis label:
ax = plt.gca()
for label in ax.xaxis.get_ticklabels():
    label.set_fontsize(20)
for label in ax.yaxis.get_ticklabels():
    label.set_fontsize(20)
myfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc',size=24) 
plt.xlabel(u'functions(number)',fontproperties=myfont)#Label x-axis
plt.ylabel(u'time(sec)',fontproperties=myfont)#Label y-axis
