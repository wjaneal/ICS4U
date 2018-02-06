# -*- coding: utf-8 -*-
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

def prime1(n):
    primes = [1]*(n+1)
    result = []
    for i in range(2,len(primes)):
        j = i
        while j < len(primes):
            if j > i:
                primes[j] = 0
            j += i

    for i in range(2,len(primes)):
        if primes[i] == 1:
            result.append(i)
    return(result)

def prime2(n):
    primes = [2]
    for i in range(3,n):
        isPrime = True
        for j in primes:
            if i % j == 0:
                isPrime = False
        if isPrime == True:
            primes.append(i)
    return(primes)

import time
import matplotlib.pyplot as plt

t = [10000,20000,30000,40000,50000]
prime1Times = []
prime2Times = []
for i in t:
    start = time.time()
    prime1(i)
    period = time.time() - start
    prime1Times.append(period)
for ii in t:
    start = time.time()
    prime2(ii)
    period = time.time() - start
    prime2Times.append(period)  

print("First Algorism:")
print("n    ", "Time")
for iii in range(0,5):
    print(t[iii], prime1Times[iii])
plt.plot(t, prime1Times)
plt.ylabel('Times take for Algorism 1')
plt.xlabel('Numbers up to')
plt.show()
print("Second Algorism:")
print("n    ", "Time")
for iiii in range(0,5):
    print(t[iiii], prime2Times[iiii])
plt.plot(t, prime2Times)
plt.ylabel('Times take for Algorism 2')
plt.xlabel('Numbers up to')
plt.show()









