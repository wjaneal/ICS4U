#-*- coding: utf-8 -*-
"""
Created on Tue Feb  6 12:51:36 2018

@author: Jeffrey

Purpose:
(1) Create two functions: prime1(n) and prime2(n) that take a number that represents the set of integers from which to find prime numbers.  For example, n=1000 specifies that the function will look for primes up to 1000.
(2) Find out how to measure elapsed time in Python
(3) Write a program that determines the amount of time taken to find primes up to the following values: n=[10000,20000,30000,40000,50000]
(4) Output of the program:
First algorithm:
n	time
10000	2.23
20000	4.67
30000 	7.88
40000	11.34
50000	14.44

Second algorithm:
n	time
10000	2.23
20000	14.67
30000 	117.88
40000	211.34
50000	11214.44

(5) Bonus:  Have Python graph the results using pyplot / matplotlib
"""
# Set up a function that process te work in the first algorism
def prime1(n):
    primes = [1]*(n+1) # Using a list that set n 1s
    result = [] # Set up an empty list that can restore results later
    for i in range(2,len(primes)): # a loop that run through all the list
        j = i
        # Eliminate non-prome numbers, set it zero
        while j < len(primes):
            if j > i:
                primes[j] = 0
            j += i
    # find and print the numbers that are marked 1
    for i in range(2,len(primes)):
        if primes[i] == 1:
            result.append(i)
    return(result)
# Set up a function that process te work in the second algorism
def prime2(n):
    primes = [2] # use the first prime number as the origin
    for i in range(3,n): # Run through up to n
        isPrime = True # make them prime as a default
        for j in primes: # Once find a fraction, make it non-prime
            if i % j == 0:
                isPrime = False
                break
        # Append prime numbers to the list
        if isPrime == True:
            primes.append(i)
    return(primes)
# Import required module
import time
import matplotlib.pyplot as plt

t = [10000,20000,30000,40000,50000]# make a list containning test numbers
prime1Times = [] # Make a list to restore results from the first algorism
prime2Times = [] # Make a list to restore results from the second algorism
# Run the first algorism for test numbers 
for i in t: 
    start = time.time()
    prime1(i)
    period = time.time() - start
    prime1Times.append(period) # restore results
# Run the second algorism for test numbers
for ii in t:
    start = time.time()
    prime2(ii)
    period = time.time() - start
    prime2Times.append(period)  # restore results
# print results lists
print("First Algorism:")
print("n    ", "Time")
for iii in range(0,5):
    print(t[iii], prime1Times[iii])
plt.plot(t, prime1Times) #plot a graph for results for first algorism
plt.ylabel('Times take for Algorism 1')
plt.xlabel('Numbers up to')
plt.show() #show the results
print("Second Algorism:")
print("n    ", "Time")
for iiii in range(0,5):
    print(t[iiii], prime2Times[iiii])
plt.plot(t, prime2Times)  #plot a graph for results for second algorism
plt.ylabel('Times take for Algorism 2')
plt.xlabel('Numbers up to')
plt.show() # show the results









