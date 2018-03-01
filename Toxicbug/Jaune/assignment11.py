# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:04:57 2018
Name: Jaune
Date: Feb.13 2018
Title: GuessingSystem
Purpose: using python to guess the number
@author: CTL
"""


import random 
import time

n = 100000 # The amount of the numbers.
number = [] # This line is to make an empty list.

for i in range(0,n): 
    number.append(random.random()) #This line is to store the i in the number list.
number.sort() # This line is to sort the list.

# These lines are to make 3 empty lists to store the time.
rt = []
lt = []
bt = []

class guess():
    
    # This line is to define a random guess function.
    def RandomGuess(w):
        # This line is to set the boundries of the data.
        maxNumber = n
        minNumber = 0
        
        while maxNumber - minNumber != 1: # This line is to create a loop.
            index = random.randint(0,n-1) # This line is to set a random number.
            if number[index] > w and index < maxNumber: 
                maxNumber = index
            if number[index] < w and index > minNumber: 
                minNumber = index                           # These four lines are to narrow down the boundry in order to find the final number.
        return(number[maxNumber])
        
    #This line is to define the linery function.
    def LinearGuess(w):
        difference = 1
        index = -1 # set a random index.
        
        for i in range(0,n-1): #This line is create a loop to search the numbers.
            if abs(number[i] - w) < difference: #This line is to make sure if the number is what we want.
                if number[i] - w > 0: # the number must be greater than the given number
                    difference = number[i] - w 
                    index = i # Make the index more and more accurate
        return(number[index])
    
    #This line is to define the binery function.
    def BineryGuess(w):
        #This line is to make two boundries.
        maxNumber = n
        minNumber = 0
        while maxNumber - minNumber != 1: #This line is to create a loop.
            index = int((maxNumber + minNumber)/2) #This line is to make the number in the middle of the data.
            if number[index] > w and w < maxNumber: 
                maxNumber = index
            if number[index] < w and index > minNumber: 
                minNumber = index                      #These four lines are to narrow down the boundries.
        return(number[maxNumber])

    #This lien is to define the time function.
    def timing(self):
        for i in range(0,5): #This line is to calculate the time that the program needs to execute.
            t0= time.time() #This line is to measure the starting time.
            guess.RandomGuess(0.7) #This line is execute the program.
            t1= time.time() #This line is to measure the ending time.
            rt.append(t1-t0) #This line is to record the time in the empty list.
        
        for a in range(0,5): #This line is to calculate the time that the program needs to execute.
            t0= time.time() #This line is to measure the starting time.
            guess.LinearGuess(0.7) #This line is execute the program.
            t1= time.time() #This line is to measure the ending time.
            lt.append(t1-t0) #This line is to record the time in the empty list.
            
        for b in range(0,5): #This line is to calculate the time that the program needs to execute.
            t0= time.time() #This line is to measure the starting time.
            guess.BineryGuess(0.7) #This line is execute the program.
            t1= time.time() #This line is to measure the ending time.
            bt.append(t1-t0) #This line is to record the time in the empty list.
    
    #This line is to define the plot function.
    def plot(self):
        print("Random Guess Algorithm:") #This line is to print the title of the diagram.
        print("trials"," ","time") #This line is to print the title of the diagram.
        for i in range(0,5):
            print(i+1," ",rt[i]) #This line is to plot the data we recorded in the diagram.
        print("\n")

        print("Linear Guess Algorithm:") #This line is to print the title of the diagram.
        print("trials"," ","time") #This line is to print the title of the diagram.
        for a in range(0,5):
            print(a+1," ",lt[a]) #This line is to plot the data we recorded in the diagram.
        print("\n")
        
        print("Binery Guess Algorithm:") #This line is to print the title of the diagram.
        print("trials"," ","time") #This line is to print the title of the diagram.
        for b in range(0,5):
            print(b+1," ",bt[b]) #This line is to plot the data we recorded in the diagram.
        print("\n")

#These lines are to execute the functions.
g=guess()
g.timing()
g.plot()
