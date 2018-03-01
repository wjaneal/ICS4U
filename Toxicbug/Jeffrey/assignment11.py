# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:00:39 2018

@author: Jeffrey

Purpose:
(1) Create a class with functions for three search algorithms - random, linear and binary. 
(2) Write a program that determines the amount of time taken to search lists of 1000000 random numbers.
(3) Sample output of the program:
"""
#import module
import random
import time

n = 100000 #How many random numbers
numberSet = [] #set up a number set to restore random list
# Using a list to generate a set of random numbers
for i in range(0,n): 
    numberSet.append(random.random())
numberSet.sort() # Sort out the list

# Set up empty lists to restore results
rResults = []
lResults = []
bResults = []

class Searching():
    
    # A function of random find
    def RandomFind(given):
        # Set up two boundries
        maxBoundry = n
        minBoundry = 0
        # Using a loop to minimize the distance between two boundries
        while maxBoundry - minBoundry != 1: # while the number difference is only two boudries, locate the number we need
            tempIndex = random.randint(0,n-1) # Set up a temparary number
            if numberSet[tempIndex] > given and tempIndex < maxBoundry: # Make the new boundry be closer and closer to the given number
                maxBoundry = tempIndex
            if numberSet[tempIndex] < given and tempIndex > minBoundry: # Make the new boundry be closer and closer to the given number
                minBoundry = tempIndex
        return(numberSet[maxBoundry])

    def LinearFind(given):
        # Set up the difference value to determine the result
        difference = 1
        index = -1 # a temparary index
        # Using a loop to loop through all the numbers
        for i in range(0,n-1):
            if abs(numberSet[i] - given) < difference: # Determine whether we need the number or not
                if numberSet[i] - given > 0: # the number must be greater than the given number
                    difference = numberSet[i] - given 
                    index = i # Make the index more and more accurate
        return(numberSet[index])
    
    def BineryFind(given):
        # Set up two boundries
        maxBoundry = n
        minBoundry = 0
        while maxBoundry - minBoundry != 1: # while the number difference is only two boudries, locate the number we need
            cIndex = int((maxBoundry + minBoundry)/2) # Set up a temparary number
            if numberSet[cIndex] > given and cIndex < maxBoundry: # Make the new boundry be closer and closer to the given number
                maxBoundry = cIndex
            if numberSet[cIndex] < given and cIndex > minBoundry: # Make the new boundry be closer and closer to the given number
                minBoundry = cIndex
        return(numberSet[maxBoundry])

# Test the function 5 times and record the data
for i in range(0,5):
    start = time.time()
    Searching.RandomFind(0.7)
    period = time.time() - start
    rResults.append(period)
# Test the function 5 times and record the data
for j in range(0,5):
    start = time.time()
    Searching.BineryFind(0.7)
    period = time.time() - start
    bResults.append(period)
# Test the function 5 times and record the data
for k in range(0,5):
    start = time.time()
    Searching.LinearFind(0.7)
    period = time.time() - start
    lResults.append(period)
# Get the avarage of those results
aveR = sum(rResults)/5
aveL = sum(lResults)/5
aveB = sum(bResults)/5
# Print results
print("Random Search Algorithm:")
print("trial#	time")
for ii in range(0,5):
    print(ii+1,"     ",  rResults[ii])
print("Average:",aveR)
print("\n")
# Print results
print("Linear Search Algorithm:")
print("trial#	time")
for jj in range(0,5):
    print(jj+1,"     ",  lResults[jj])
print("Average:",aveL)
print("\n")
# Print results
print("Binary Search algorithm:")
print("trial#	time")
for kk in range(0,5):
    print(kk+1,"     ",  bResults[kk])
print("Average:",aveB)





