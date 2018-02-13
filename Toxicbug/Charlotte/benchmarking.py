#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name:Charlotte Chen
Date:Created on Mon Feb  5 12:44:32 2018
Title:Benchmarking Algorithms
Purpose:
(1) Create two functions: prime1(n) and prime2(n) that take a number that represents the set of integers from which to find prime numbers.  For example, n=1000 specifies that the function will look for primes up to 1000.
(2) Find out how to measure elapsed time in Python
(3) Write a program that determines the amount of time taken to find primes up to the following values: n=[10000,20000,30000,40000,50000]
"""
integerRange=[10000,20000,30000,40000,50000]#This list contains the integer values used to test the algorithms.
import time
import matplotlib.pyplot as plt
timePrime1=[] #This creates an empty list for the first algorithm.
timePrime2=[] #This creates an empty list for the second algorithm.
prime=[] #This creates an empty list for prime numbers.
#This function tests the efficiency of the second algorithm.
def prime2(n):
    startTime=time.time() #This gets the start time.
    primes=[1]*(n+1) #This creates a list of 1s.
    for x in range(2,len(primes)): #This loop iterates through the list from the third element.
        if primes[x]==0: #If this number is already a multiple of a number, it can be skipped.
            break
        j=x
        while j < len(primes): #This loop iterates through the list.
            if j>x:
                primes[j]=0 #If this number is a multiple of x, this number is not a prime number.
            j+=x #This goes to the next multiple of x.
    #This loop iterates through the list.
    for y in range(2,len(primes)):
        #If this number is not a multiple of any other number, it is a prime number.
        if primes[y]!=0:
            prime.append(y) #This adds the number into the list containing primes.
    timePrime2.append((n,time.time()-startTime)) #This calculates the execution time of this function and adds the range and time to the list.
#This function tests the efficiency of the first algorithm.
def prime1(n):
    startTime=time.time() #This gets the start time.
    primes=[2] #This creates a list for the prime numbers.
    for i in range(3,n+1):
        isPrime=True #This initializes isPrime as True.
        for j in primes: #This loop iterates through the list containing primes.
            if i % j == 0: #If this number is a multiple of a prime, it is not a prime number.
                isPrime=False #This sets isPrime to False.
                break #Once it finds that this number is a multiple of a prime, it goes to the next number.
        if isPrime==True: #If a number is not a multiple of any prime number, it is a prime number.
            primes.append(i) #This adds the number to the list containing primes.
    timePrime1.append((n,time.time()-startTime)) #This calculates the execution time of this function and adds the range and time to the list.
#This loop tests the algorithms with several integer values respectively.
for i in integerRange:
    prime1(i)
    prime2(i)
#This part prints the integer range and time for the first algorithm.
print("First algorithm:")
print("n"+"         "+"time")
for i in range(0,len(timePrime1)):
    print(str(timePrime1[i][0])+"     "+str(timePrime1[i][1]))
#This part prints the integer range and time for the second algorithm.
print("Second algorithm:")
print("n"+"         "+"time")
for i in range(0,len(timePrime2)):
    print(str(timePrime2[i][0])+"     "+str(timePrime2[i][1]))
#This part uses python to graph the data.
time1=[]
nValue=[]
for i in timePrime1:
    nValue.append(i[0])
    time1.append(i[1])
plt.plot(nValue, time1)#This plots the graph for algorithm 1 based on n value and time.
plt.title('Algorithm')
plt.ylabel('time')
plt.xlabel('nValue')
plt.show()

time2=[]
for i in timePrime2:
    time2.append(i[1])
plt.title('Algorithm2')
plt.plot(nValue, time2)#This plots the graph for algorithm 2 based on n value and time.
plt.ylabel('time')
plt.xlabel('nValue')
plt.show()

time1=[]
nValue=[]
#This loop appends the x and y values to the list to draw a graph for the first algorithm.
for i in timePrime1:
    nValue.append(i[0])
    time1.append(i[1])
time2=[]
#This loop appends the y values to the list to draw a graph for the second algorithm.
for i in timePrime2:
    time2.append(i[1])
plt.plot(nValue, time1,color='red') #This draws a red line for the first algorithm.
plt.plot(nValue,time2,color='blue') #This draws a blue line for the second algorithm.
plt.title('Benchmarking Algorithms') #This creates a title for the graph.
plt.ylabel('time') #This sets the label for the y-axis.
plt.xlabel('nValue') #This sets the label for the x-axis.
plt.show()
