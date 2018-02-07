#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 12:42:19 2018

@author: Mandy

#Program Title: A9 Primes

(1) Create two functions: prime1(n) and prime2(n) that take a number that represents the set of integers from which to find prime numbers.  For example, n=1000 specifies that the function will look for primes up to 1000.
(2) Find out how to measure elapsed time in Python
(3) Write a program that determines the amount of time taken to find primes up to the following values: n=[10000,20000,30000,40000,50000]
(4) Output of the program:
First algorithm:
n       time
10000   2.23
20000   4.67
30000   7.88
40000   11.34
50000   14.44
"""

import time
n = [10000,20000,30000,40000,50000]
a1times = []
a3times = []

def P1(n):
    #t0 = time.time()
    primes = [2]
    for i in range (3,n):
        for j in primes:
            if i % j == 0:
                break
            if j == primes[-1]:
                primes.append(i)
    #print(primes)
    #t1 = time.time()
    #total = t1-t0
    #print(total)


def P3(n):
    #t0 = time.time()
    number = [1] * (n+1)
    prime3 = []
    for i in range (2, len(number)):
        j = i
        while j < len(number):
            if j > i:
                number[j] = 0
            j += i
    for i in range (2, len(number)):
        if number[i] != 0:
            prime3.append(i)
            #t1 = time.time()
            #total3 = t1-t0
    #print(total3)
############################
# print diagrams
print("First Algorithm")
print("n","         ","time")
for z in range(0, len(n)) :
    t0 = time.time()
    P1(n[z])
    t1 = time.time()
    total = t1-t0
    a1times.append(total)
    print(n[z],"    ",total)
print("               ")   
print("Second Algorithm")
print("n","         ","time")
for z in range(0, len(n)) :
    t0 = time.time()
    P3(n[z])
    t1 = time.time()
    total = t1-t0
    a3times.append(total)
    print(n[z],"    ",total)
###########################
    
#draw diagrams

import pylab as pl
 
pl.plot(n, a1times)# use pylab to plot x and y
pl.show()# show the plot on the screen

pl.plot(n, a3times)
pl.show()
