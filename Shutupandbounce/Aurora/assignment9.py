'''
Assignment 9 - Benchmarking Algorithms
Coding convention: 
(a) lower case file name
(b) Name:Aurora  Date：2018/02/06
(c) mixedCase variable names
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
'''
Number = [10000,20000,30000,40000,50000]#This is the list of the maximum in the range of time taken to find primes.
time1 = []#this is the time list1
time2 = []#this is the time list2
prime1 = [2]
maxj = 2
#Import the time module
import time
#This is prime1
for n in Number:    
    start1 =time.time() #This starts recording time
    for i in range(3,int(n)):
        isprime = True
        for j in prime1:
            if i % j == 0:
                isprime = False
                if isprime == True:
                    prime1.append(i)
    end1 = time.time() #This is the end of recording
    X = end1 - start1
    time1.append(X)
#this is the prime2
for m in Number:
    start2 = time.time() #This starts recording time
    for i in range(2,m):
        for temp in range(2,i):
            if i%temp==0:
                break
            if temp==i-1:
                prime2.append(i)
    end2 = time.time() #This is the end of recording
    X2 = end2 - start2
    time2.append(X2)
#This is the data processing area
print("  First Algorithm: \n   n           time")
for n,T1 in zip(Number,time1):
    print(" ",n,"      ",T1)
    #This is to print the data of the first algorithm in rows
print("\n  Second Algorithm: \n   n           time")
for m,T2 in zip(Number,time2):
    print(" ",m,"      ",T2)
    #This is to print the data of the second algorithm in rows

#Import the module
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('fivethirtyeight')
plt.title('Execution time of two algorithms')
plt.xlabel('Range')
plt.ylabel('Time(Seconds)')
x = Number
y1 = time1
y2 = time2
plt.figure(1)
plt.subplot(211)
plt.plot(x, y1)

plt.subplot(212)
plt.plot(x, y2)
plt.show()
