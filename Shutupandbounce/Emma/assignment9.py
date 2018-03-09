# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 13:49:48 2018
@author: Emma
Assignment 9 - Benchmarking Algorithms
Coding convention: 
(b) Purpose:(1) Create two functions: prime1(n) 
and prime2(n) that take a number that represents the set of 
integers from which to find prime numbers. 
(2) Find out how to measure elapsed time in Python
(3) Write a program that determines the amount 
of time taken to find primes up to the 
following values: n=[10000,20000,30000,40000,50000]
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
(5) Bonus:  Have Python graph the results 
using pyplot / matplotlib

"""
#Import resource required
from timeit import timeit
import matplotlib
import matplotlib.pyplot as plt
#Set the variables for 5 calculation
ran = [10000,20000,30000,40000,50000]#gather the values up for convenience of displaying the outcome
a1time = []#create 2 sets of time taken by calculating each value in r from 2 different algorithms
a2time = []
def func1(self):
    for k in ran:
        p = [2]#set the min. of prime number to 2
        for i in range(3,[n[k]]+1):#using a for loop to set the number range
            isPrime = True#whichever the prime number is is True
            for j in p:#in prime number
                if i % j == 0:#if the number divided by prime number has no remainder
                    isPrime = False#then the number is not prime
                    break
            if  isPrime == True:#if it is
                p.append(i)#add it to the original set of prime
    #print(primes)#display all the prime we have
    # timeit(function name，running environment，
#        number=how many time we run the program)
    t = timeit('func1()', 'from __main__ import func1', number=1)
    a1time.append(t)#time for 5 times and add them to a timeset
    
def func2(self):# Solving using sieve of erastothenes
    p = [1]*(n+1)
    for i in range(2, len(p)):#in the list of 3rd element:
        if p[i]==0: #If this number is already a multiple of a number, it can be skipped.
            break
        j = i
        while j <len(p):#as long as j< the length of prime list:
            if j>i:#if j = multiple of i:
                p[j] = 0# there will not be a prime number.
            j+=i#divisors added
    for i in range(2, len(p)):
        if p[i] != 0:#if it cannot be a multiple:
            print(i)#it is a pn
    tt = timeit('func2()', 'from __main__ import func2', number=1)
    a2time.append(tt)

#create a function to display the outcome
def output():
    for i in range(0,len(a1time)):
        print("algorithm 1 result:\n", " n      time(sec)")
        print(str(ran[i][0])+"  "+str(a1time[i][1]))
    for j in range(0,len(a2time)):
        print("algorithm 2 result:\n", " n      time(sec)")    
        print(str(ran[j][0])+"  "+str(a2time[j[1]]))

for i in ran:
    func1(i)
    func2(i)
#run the program for displaying  
output()
#make a title for the graph
plt.title("Benchmarking Algorithms")
#plot the time(x-value(s),y-value(s),the style(red dots) of graph)
plt.plot(ran,[a1time,a2time],'ro:')
#change the size of the axis label:
ax = plt.gca()
for label in ax.xaxis.get_ticklabels():
    label.set_fontsize(20)
for label in ax.yaxis.get_ticklabels():
    label.set_fontsize(20)
myfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/simsun.ttc',size=24) 
plt.xlabel(u'functions(number)',fontproperties=myfont)#label x-axis
plt.ylabel(u'time(sec)',fontproperties=myfont)#label y-axis
