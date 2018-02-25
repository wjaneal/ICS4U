# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Name:Henry
Date: 16/Feb/2018
Program Title:  Recursive Algorithms

Purpose:
(1) Create a class with functions for three recursive algorithms.
(2)Include factorials, the Towers of Hanoi and any other recursive function.
(3)Allow the user to choose any of the three functions and then interact with the function.
(4)The program should provide adequate instructions and output to be useful.
"""
class recursion: #This create a class for three recursive algorithms
    def factorial(self,N): #This define a function for calculating fatorials
        if N==0 or N==1: #The fatorial is 1
            return 1
        else:
            return N*self.factorial(N-1)
        
    def hanoi(self,n, source, helper, target):#This defines a function for playing the Towers of Hanoi game.
        if n==1 : #If there is only one disk, its movement should be printed.
            print(source,"->",target)
        else:
            #move tower of size n - 1 to helper:
            self.hanoi(n-1, source, target, helper)
            self.hanoi(1, source, helper, target)
            #move tower of size n - 1 from helper to target
            self.hanoi(n-1,helper, source, target)

    def Fibonacci(self,n):#This defines a function for calculating the Fibonacci sequence.
        if n == 1 or n == 2: # The first and second item in the Fibonacci sequence are 1.
            return 1
        if n > 2:
            return self.Fibonacci(n-1)+self.Fibonacci(n-2)# each number in the sequence is the sum of the two preceding numbers.
    
    
    def interactions(self): #This function allows the user to interact with the recursive algorithms.
            print("Which one would you like to choose?") 
            print("Input Factorial for Factorial")
            print("Input Hanoi for The Towers of Hanoi")
            print("Input Fibonacci for Fibonacci sequence")
            #This prints some instructions to allow the user to choose a function.
            Start = input() #This lets the user input the choice.
            if Start=='Factorial':
                print("Welcome to the Factorial Calculator!")
                n = int(input("Which number would you like to calculate the factorial of?")) #This asks the user the number he/she wants to calculate the factorial of.
                print("The factorial of "+str(n)+" is "+str(self.factorial(n))) #This prints the factorial of the number.
            if Start=='Hanoi':
                print("Welcome to the Towers of Hanoi game!")
                print("The objective of the puzzle is to move the entire stack to another rod.")
                N=int(input("How many disks would you like to have?"))
                rods=input("How would you like to call the three rods (first,second,third) in the game? (Please separate them with spaces)").split()
                print("This shows how you should move your disks:")
                self.hanoi(N,rods[0],rods[1],rods[2]) #This prints the steps of moving the disks.
            if Start=='Fibonacci':
                print("Welcome to the Fibonacci sequence!")
                print("The Fibonacci sequence is a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers.")
                n=int(input("How many terms in the Fibonacci sequence would you like to calculate?"))
                print("These are the first "+str(n)+" terms of the Fibonacci sequence")
                #This prints the Fibonacci sequence.
                for i in range(1,n+1):
                    print(self.Fibonacci(i))

                    
r=recursion() 
r.interactions() #Let's start