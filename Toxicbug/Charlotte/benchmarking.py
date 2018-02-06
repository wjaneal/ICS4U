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
integerRange=[10000,20000,30000,40000,50000]
import time
import matplotlib.pyplot as plt
timePrime1=[]
timePrime2=[]
prime=[]
def prime2(n):
    startTime=time.time()
    primes=[1]*(n+1)
    for x in range(2,len(primes)):
        if primes[x]==0:
            break
        j=x
        while j < len(primes):
            if j>x:
                primes[j]=0
            j+=x
    for y in range(2,len(primes)):
        if primes[y]!=0:
            prime.append(y)
    timePrime2.append((n,time.time()-startTime))
def prime1(n):
    startTime=time.time()
    primes=[2]
    for i in range(3,n+1):
        isPrime=True
        for j in primes:
            if i % j == 0:
                isPrime=False
                break
        if isPrime==True:
            primes.append(i)
    #print(primes)
    timePrime1.append((n,time.time()-startTime))
for i in integerRange:
    prime1(i)
    prime2(i)
print("First algorithm:")
print("n"+"         "+"time")
for i in range(0,len(timePrime1)):
    print(str(timePrime1[i][0])+"     "+str(timePrime1[i][1]))
print("Second algorithm:")
print("n"+"         "+"time")
for i in range(0,len(timePrime2)):
    print(str(timePrime2[i][0])+"     "+str(timePrime2[i][1]))

#This part uses python to graph the data.
'''time1=[]
nValue=[]
for i in timePrime1:
    nValue.append(i[0])
    time1.append(i[1])
plt.plot(nValue, time1)
plt.title('Algorithm')
plt.ylabel('time')
plt.xlabel('nValue')
plt.show()

time2=[]
for i in timePrime2:
    time2.append(i[1])
plt.title('Algorithm2')
plt.plot(nValue, time2)
plt.ylabel('time')
plt.xlabel('nValue')
plt.show()
'''
time1=[]
nValue=[]
for i in timePrime1:
    nValue.append(i[0])
    time1.append(i[1])
time2=[]
for i in timePrime2:
    time2.append(i[1])
plt.plot(nValue, time1,color='red')
plt.plot(nValue,time2,color='blue')
plt.title('Benchmarking Algorithms')
plt.ylabel('time')
plt.xlabel('nValue')
plt.show()
