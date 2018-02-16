#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: chenquancheng
Date: Created on Fri Feb 16 11:06:07 2018
Title: Recursive Algorithms
Purpose: (1) Create a class with functions for three recursive algorithms.  
(2)Include factorials, the Towers of Hanoi and any other recursive function.  
(3)Allow the user to choose any of the three functions and then interact with the function.  
(4)The program should provide adequate instructions and output to be useful.
"""
from functools import lru_cache #This imports the tool for Memoization.
class recursion: #This creates a class for three recursive algorithms.
    def fact(self,n): #This defines a function for calculating factorials.
        if n==1: #The factorial of 1 is 1.
            return 1
        else:
            return n*self.fact(n-1) #This calls the function itself.
    
    @lru_cache(maxsize = 1000) #This allows the program to store the results that have been calculated to speed itself up.
    def Fibonacci(self,n): #This defines a function for calculating the Fibonacci sequence.
        if n == 1: #The first item in the Fibonacci sequence is 1.
            return 1
        if n == 2: #The second item in the Fibonacci sequence is 1.
            return 1
        if n > 2:
            return self.Fibonacci(n-1)+self.Fibonacci(n-2) #Each number (starting from the third item) is the sum of the two preceding numbers.
    
    def tower(self,N,beg,aux,end): #This defines a function for playing the Towers of Hanoi game.
        if N==1: #If there is only one disk, its movement should be printed.
            print(beg,"->",end)
        else:
            self.tower(N-1,beg,end,aux)
            self.tower(1,beg,aux,end)
            self.tower(N-1,aux,beg,end)
    
    def interactions(self): #This function allows the user to interact with the recursive algorithms.
        self.endGame=False #This initializes self.endGame to False.
        while(self.endGame==False): #This loop continues if self.endGame is False 
            print("Which function would you like to use?") 
            print("Type F for Factorials")
            print("Type T for The Towers of Hanoi")
            print("Type S for Fibonacci sequence")
            print("Type E if you want to exit the program.")
            #This prints some instructions to allow the user to choose a function.
            choice=input() #This lets the user input his/her choice.
            if choice=='F':
                print("Welcome to the Factorial Calculator!")
                n=int(input("Which number would you like to calculate the factorial of?")) #This asks the user the number he/she wants to calculate the factorial of.
                print("The factorial of "+str(n)+" is "+str(self.fact(n))) #This prints the factorial of the number.
            if choice=='T':
                print("Welcome to the Towers of Hanoi game!")
                print("The objective of the puzzle is to move the entire stack to another rod.")
                N=int(input("How many disks would you like to have?"))
                rods=input("How would you like to call the three rods (first,second,third) in the game? (Please separate them with spaces)").split()
                print("This shows how you should move your disks:")
                self.tower(N,rods[0],rods[1],rods[2]) #This prints the steps of moving the disks.
            if choice=='S':
                print("Welcome to the Fibonacci sequence!")
                print("The Fibonacci sequence is a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers.")
                n=int(input("How many terms in the Fibonacci sequence would you like to calculate?"))
                print("These are the first "+str(n)+" terms of the Fibonacci sequence")
                #This prints the Fibonacci sequence.
                for i in range(1,n+1):
                    print(self.Fibonacci(i))
            if choice=='E':
                self.endGame=True #This ends the game.
            else:
                continue #If the input does not match any of the above conditions, asks the user to input again.
                    
r=recursion() #This creates an instance of the recursion class.
r.interactions() #This starts the program.