#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:08:24 2018

@author: xuwentong
"""

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