#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:38:07 2018
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
@author: haichunkan
"""
import time
import matplotlib.pyplot as plt
n=[10000,20000,30000,40000,50000]

def primeOne(m1):#the first function to find primes
    prime=[2]
    for i in range(3,m1):
        for j in prime:
            if i% j==0:
                break
            if j== prime[-1]:
                prime.append(i) 
    return()
def primeTwo(m2):#The second function to find primes.
    newprime=[]
    prime=[1]*(m2+1)
    for i in range(2,len(prime)):
        j=i
        while j<len(prime):
            if j>i:
                prime[j]=0
            j+=i
    for i in range(2,len(prime)):
        if prime[i]!=0:
            newprime.append(prime[i])
    return()       
def countTime():#Measure the time that function primeOne() takes.
    k1=[]
    e1=[]
    print("First algorithm:")
    print("n    time")
    for i in range(0,len(n)):
        m1=n[i]
        k1.append(m1)
        start_time1 = time.time()#start the time
        primeOne(m1)
        elapsed_time1 = time.time() - start_time1#end the timer
        e1.append(elapsed_time1)
        print(m1,elapsed_time1)
        
    k2=[]
    e2=[]
    print("Second algorithm:")
    print("n    time")
    for i in range(0,len(n)):
        m2=n[i]
        k2.append(m2)
        start_time2 = time.time()
        primeTwo(m2)
        elapsed_time2 = time.time() - start_time2
        e2.append(elapsed_time2)
        print(m2,elapsed_time2)
    plt.plot(k1, e1, color='green')
    plt.plot(k2, e2, color='orange')
    plt.xlabel('under number n')
    plt.ylabel('time needed')
    plt.title('haha')
    plt.show()
    return()
countTime() #Run the program.       

