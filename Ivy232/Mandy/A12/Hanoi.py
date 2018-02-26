#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:08:24 2018
 
Assignment 12 - Recursive Algorithms - Towers of Hanoi

(1) Create a class with functions for three recursive algorithms.  Include factorials, the Towers of Hanoi and any other recursive function.  Allow the user to choose any of the three functions and then interact with the function.  The program should provide adequate instructions and output to be useful.

@author: Mandy
"""

#Factorials
def f(n):
    if n > 1:
        return n * f(n-1)
    else:
        return 1
x = int(input("Factorial: n!, n = "))
print(f(x))
print()

#Hanoi
def Hanoi (n,p1,p2): # n: number of pieces that you want to move
    posts = [p1,p2] # p1: the current position;# p2: the target position
    
    while True: # p3: the third position
        if 1 not in posts:
            p3 = 1
        if 2 not in posts:
            p3 = 2
        if 3 not in posts:
            p3 = 3
        break
    
    if n > 1:
        Hanoi(n-1,p1,p3) # Step One: move all (n-1) pieces to the third position.
        print ("move one from", p1 ,"to", p2) # Step Two: move the last longest piece to the target position.
        Hanoi(n-1,p3,p2) # Step Three: move all (n-1) pieces from the third position to the target position.
    elif n == 1:  
        print ("move one from", p1 ,"to", p2)
    else:
        print("Sorry! n can't be samller than 1!")
    
###############testing############################################################
print("You have three positions:1 ,2, 3 to place your circles")
n = int(input("Please enter a number of pieces that you want to move:"))

currentPosition = int(input("Please enter the number of your current position:"))
targetPosition = int(input("Please enter the number of your target position:"))

print(" ")

print("please follow the instructions to move the circles!")
print(Hanoi(n,currentPosition,targetPosition))
import random
n = []
for i in range(0,1000):
    n.append(random.random())
    n.sort()
print()

#Recursive algorithms in Binary
import random
n = []
for i in range(0,1000):
    n.append(random.random())
    n.sort()    
def Binary(n):
        
    mid = len(n)//2
    LH = []
    RH = []
        
    if n[mid] > 0.7:
        LH = n[:mid+1]
        #print("LH",LH)
        #print("1",LH)
        if len(LH) == 2:
            #print(LH)
            print ("Result",LH[1])
            pass
        else:
            Binary(LH)  
            #print("3",LH)
    elif n[mid] < 0.7:
        RH = n[mid:]
        #print(RH)
        #print("4",RH)
        if len(RH) == 2:
            #print("RH",RH)
            print("Result",RH[1])
            pass
        else:
            Binary(RH)
            #print("6",RH)
    


#print("n",n)
Binary(n)

