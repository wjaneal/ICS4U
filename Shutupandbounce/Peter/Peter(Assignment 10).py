#Assignment 10 - Benchmarking Sorting Algorithms
#Name:Peter Zeng
#Date: February,13 2018
#Program Title:Benchmarking Sorting Algorithms
#Program Function:(1) Create a class with functions for three sorting algorithms
# - bubble sort, selection sort and insertion sort. 
#(2) Write a program that determines the amount of time taken to sort lists of 
#random numbers of the following lenghs: n=[10000,20000,30000,40000,50000]
#(3) Output of the program:
import time
import matplotlib.pyplot as plt
import random
import pylab as l

#sorting algorithm
class sorting:
    #This part is used to garph the data to indicate how much time the algorithms used
    n = [10000,20000,30000,40000,50000]
    time1 = []
    time2 = []
    time3 = []
    def bubble_sort(list):# it rearrange the list from the unexpected list for random numbers
        randomnum = len(list)
        for i in range(0,randomnum-1):   
            for j in range(0, randomnum-1-i): 
                if list[j] > list[j + 1]:
                    swap = list[j]
                    list[j] = list[j+1]   # let those value combine to each others
                    list[j+1] = swap

    #matplotlib part
    print("The Bubble Sort")
    print("n","         ","time")
    for t in range(0, len(n)):
        for p in n:
            list = random.sample(range(p), 10)
            start = time.time()
            bubble_sort(list)
            after = time.time()
            total = start - after
        time1.append(total)
        print(n[t],"    ",total)
    plt.ylabel('Running Time For Algorithm 1')
    plt.xlabel('Numbers')
    l.plot(n, time1)
    l.show()        #show the data

    list = [10,25,34,8,28,56,78,95,99]   # print out for this algorithm, and test it
    bubble_sort(list)                  
    print(list)
  

    def selection_sort(list1): #it can select the biggest number to right side,then the smallest numbers to left side
        for magic in range(len(list1)-1,0,-1):
            Max = 0
            for town in range(1,magic + 1):
                if list1[town] > list1[Max]:
                    Max = town
                    select = list1[town]
                    list1[magic] = list1[Max]
                    list1[Max] = select
    #matplotlib part
    print("The Selection Sort")
    print("n","         ","time")
    for t in range(0, len(n)):
        for e in n:
            list = random.sample(range(e), 10)
            start = time.time()
            selection_sort(list)
            after = time.time()
            total = start-after
        time2.append(total)
        print(n[t],"    ",total)
    plt.ylabel('Running Time For Algorithm 2')
    plt.xlabel('Numbers')
    l.plot(n, time2)
    l.show()          #show the data
    
    list1 = [10,25,22,8,28,56,78,95,99,69]     # print out for this algorithm, and test it
    selection_sort(list1)
    print(list1)

    def insertion_sort(list2):            #it builds the final sorted array (or list) one item at one time
        for index in range(1,len(list2)):
            things = list2[index]
            p = index
            while p > 0 and list2[p - 1] > things:
                list2[p] = list2[p-1]
                p = p - 1
                list2[p] = things
    #matplotlib part
    print("The Insertion Sort")
    print("n","         ","time")
    for t in range(0, len(n)):
        for r in n:
            list = random.sample(range(r), 10)
            start = time.time()
            insertion_sort(list)
            after = time.time()
            total = start - after
        time3.append(total)
        print(n[t],"    ",total)
    plt.ylabel('Running Time For Algorithm ')
    plt.xlabel('time')
    l.plot(n, time3)
    l.show()      # show the data
    
    list2 = [10,25,34,8,55,56,78,95,99,69]     # print out for this algorithm, and test it
    insertion_sort(list2)
    print(list2)






   
    





