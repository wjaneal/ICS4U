#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:08:24 2018
 
Assignment 12 - Recursive Algorithms - Towers of Hanoi

(1) Create a class with functions for three recursive algorithms.  Include factorials, the Towers of Hanoi and any other recursive function.  Allow the user to choose any of the three functions and then interact with the function.  The program should provide adequate instructions and output to be useful.

@author: Mandy
"""
class Recusive: # define a class with three functions.
    
    #Factorials
    def f(self,n):
        if n > 1: # n! = n*(n-1)! = n*(n-1)*(n-2)! = ...
            return n * self.f(n-1)
        else:
            return 1

    #Hanoi
    def Hanoi (self,n,p1,p2): # n: number of pieces that you want to move
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
            self.Hanoi(n-1,p1,p3) # Step One: move all (n-1) pieces to the third position.
            print ("move one from", p1 ,"to", p2) # Step Two: move the last longest piece to the target position.
            self.Hanoi(n-1,p3,p2) # Step Three: move all (n-1) pieces from the third position to the target position.
        elif n == 1:  
            print ("move one from", p1 ,"to", p2)
        else:
            print("Sorry! n can't be samller than 1!")
            
  
        
    #Fibonacci Number
    def fib(self,n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
    
    
    def interactions(self): # interact with the recursive algorithms
        self.endGame = False # this initializes self.endGame to False.
        while(self.endGame == False): #This loop continues if self.endGame is False 
            print("Please choose a fuction to play with!") 
            print("Type f for Factorials")
            print("Type h for T Hanoi Instructions")
            print("Type F for Fibonacci Number")
            print("Type e if you want to exit the program.")
            choice=input() # allow the user to input the choice.
            if choice=='f':
                print("n!")
                n=int(input("n:")) 
                print("The factorial of "+str(n)+" is "+str(self.f(n))) 
            if choice=='h':
                print(" Hanoi Tower!")
                print("You have three positions:1 ,2, 3 to place your circles")
                i = int(input("Please enter a number of pieces that you want to move:"))
                currentPosition = int(input("Please enter the number of your current position:"))
                targetPosition = int(input("Please enter the number of your target position:"))
                print(" ")
                print("please follow the instructions to move the circles!")
                print(self.Hanoi(i,currentPosition,targetPosition))
                print()
            if choice=='F':
                print(" Fibonacci Number! ")
                print("Here you can find the n th Fibonacci Number. (0 is the  first Fibonacci Number)")
                m = int(input("m:"))
                print(self.fib(m))
                
            if choice=='e':
                self.endGame=True # quit
            else:
                continue #If the input does not match, asks the user to input again.
                    
a = Recusive() # create an instance in the class
a.interactions() # start  

