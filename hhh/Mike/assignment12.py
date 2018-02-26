# -*- coding: utf-8 -*-
"""
Name: Xu, Yingjie (Mike)
Date: 2018-02-24
Program Title: assignment12 (Recursive Algorithms)
Purpose: 
(1) Create a class with functions for three recursive algorithms.  
(2)Include factorials, the Towers of Hanoi and any other recursive function.  
(3)Allow the user to choose any of the three functions and then interact with the function.  
(4)The program should provide adequate instructions and output to be useful.
"""

class recursive_algorithms: #This creates a class for three recursive algorithms.
        
    #This defines a function for playing the Towers of Hanoi game.
    def tower_of_hanoi(self,N,source,helper,target): 
        if N==1: #If there is only one disk, its movement should be printed.
            print(source,"->",target)
        else:
            self.tower_of_hanoi(N-1,source,target,helper)
            self.tower_of_hanoi(1,source,helper,target)
            self.tower_of_hanoi(N-1,helper,source,target)
            
    #This defines a function for calculating the Fibonacci sequence.        
    def fibonacci_sequenece(self,n): 
        if n == 1: #The first item in the Fibonacci sequence is 1.
            return 1
        if n == 2: #The second item in the Fibonacci sequence is 1.
            return 1
        if n > 2: #This calculates some more items in the sequence
            return self.fibonacci_sequenece(n-1)+self.fibonacci_sequenece(n-2) 
       
    #This defines a function for calculating factorials.
    def factorial(self,n):
        if n==1: #The factorial of 1 is 1.
            return 1
        else:
            return n*self.fact(n-1) #This calls the function itself.

    #This function allows the user to use the program.    
    def interaction(self): 
        print("Please choose a function: Press 1 for Factorials, press 2 for The Towers of Hanoi, press 3 for Fibonacci sequence") 
        #This prints some instructions to allow the user to choose a function.
        number=input() #This lets the user input his/her choice.
        
        if number=='1':
            print("The Factorial Calculator!")
            n=int(input("Please input the number: ")) #This asks the user the number he/she wants to calculate the factorial of.
            print("The factorial of "+str(n)+" is "+str(self.fact(n))) #This prints the factorial of the number.
            
        if number=='2':
            print("The Towers of Hanoi game!")
            N=int(input("Please input number of disks: "))
            stick=['stick1','stick2','stick3']
            print("This shows how you should move your disks:")
            self.tower_of_hanoi(N,stick[0],stick[1],stick[2]) #This prints the steps of moving the disks.
            
        if number=='3':
            print("The Fibonacci sequence!")
            n=int(input("Please enter the items you would like to calculate: "))
            #This prints the Fibonacci sequence.
            for i in range(1,n+1):
                print('The number '+str(i)+' item is '+str(self.fibonacci_sequenece(i))+' ')
                    
r=recursive_algorithms() #This runs the program.
r.interaction() #This starts the program.