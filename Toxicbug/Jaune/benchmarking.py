# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 12:39:56 2018
Name:Jaune 
Date:Feb. 6
Title: Benchmarking
Purpose:Studying
@author: CTL
"""

import time
import pylab as pl
n=[1000,2000]
p1time=[]
p2time=[]

#To define two functions that can help find prime number
def prime1(n):
    primes=[1]*(n+1)

    for i in range(2,len(primes)):
        j=i
        while j<len(primes):
            if j>i:
                primes[j]=0
            j+=i
    for i in range(2,len(primes)):
        if primes[i] !=0:
            return(i)
            
def prime2(n):
    primes = [2]
    for i in range(3,n):
        isPrime = True
        for j in primes:
            if i%j == 0:
                isPrime = False
                break
        if isPrime == True:
            primes.append(i)
    return(primes)

#To make the figures form tables
print("First Algorithm")
print("n"," ","time")
for i in n:
    t0=time.time()
    prime1(i)
    t1=time.time()
    t=t1-t0
    p1time.append(t)
    print(i," ",t)
pl.plot(n, p1time)
pl.xlabel('Numbers')
pl.ylabel('Time')
pl.show()

print("              ")
print("Second Algorithm")
print("n"," ","time")
for a in n:
    t0=time.time()
    prime2(a)
    t1=time.time()
    t=t1-t0
    p2time.append(t)
    print(a," ",t)
pl.plot(n, p2time)
pl.xlabel('Numbers')
pl.ylabel('Time')
pl.show()
