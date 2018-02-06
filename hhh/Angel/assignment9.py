#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:40:11 2018
@author: hailankan
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
Title: find primes
"""
import matplotlib.pyplot as plt
import time
n=[10000,20000,30000,40000,50000,100000,200000]

def FirAl():
    totalTime=[]
    print('First algorithm:')
    print('n	time')
    for item in n:#loop for each value in the n list
        start_time = time.time()
        prime=[2]
        for i in range(3,item):
            for j in prime:
                if i % j == 0:
                    break#stop for multiples
            if j == prime[-1]:
                prime.append(i)#append primes
        elapsed_time = time.time() - start_time
        totalTime.append(elapsed_time)
        print(item, elapsed_time)
    plt.plot(n,totalTime)
    plt.show()
    

def SecAl():
    totalTime=[]
    print('Second algorithm:')
    print('n	time')
    for item in n:
        start_time = time.time()
        prime = [2]
        for i in range(3,item):
            for j in range(0,len(prime)):
                if i % prime[j]== 0:
                    break
            if j == len(prime)-1:
                prime.append(i)
        elapsed_time = time.time() - start_time#measure the time
        totalTime.append(elapsed_time)
        print(item, elapsed_time)#print time used
    plt.plot(n,totalTime)
    plt.show()


def ThiAl():
    totalTime=[]
    print('Third algorithm:')
    print('n	time')
    for item in n:
        start_time = time.time()
        prime=[]
        number=[]
        for i in range(2,item):
            number.append(i)
        for j in range(0,len(number)):
            j = i
            while j < len(number):
                if j > i:
                    number[j] = 0
                j+=i
        for i in range(2,len(number)):
            if number[i]!=0:
                prime.append(i)
        elapsed_time = time.time() - start_time
        totalTime.append(elapsed_time)
        print(item, elapsed_time)
    plt.plot(n,totalTime)
    plt.show()


FirAl()
SecAl()
ThiAl()

