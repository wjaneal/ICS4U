# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 13:03:29 2018

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
bt = []

class guess():
    
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
    def timing():
            
        for b in range(0,5): #This line is to calculate the time that the program needs to execute.
            t0= time.time() #This line is to measure the starting time.
            guess.BineryGuess(0.7) #This line is execute the program.
            t1= time.time() #This line is to measure the ending time.
            bt.append(t1-t0) #This line is to record the time in the empty list.
    
    #This line is to define the plot function.
    def plot():
        
        print("Binery Guess Algorithm:") #This line is to print the title of the diagram.
        print("trials"," ","time") #This line is to print the title of the diagram.
        for b in range(0,5):
            print(b+1," ",bt[b]) #This line is to plot the data we recorded in the diagram.
        print("\n")

#These lines are to execute the functions.
g=guess()
g.timing()
g.plot()