# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:50:15 2018
Name: Jaune
Date: Feb 16
Title: Recursive Algorithm
Purpose: Learn to know recursive function

Create a class with functions for three recursive algorithms. 
 Include factorials, the Towers of Hanoi and any other recursive function. 
 Allow the user to choose any of the three functions and then interact with the function. 
 The program should provide adequate instructions and output to be useful.
 

@author: CTL
"""

class recursivealgorithm():
    
    def factorial(self,n):
        if n>1: #This line is to compare the variable n to 1.
            return n*self.factorial(n-1) #This line is to call the function itself and to calculate.
        else:
            return 1 #This line is to make the last number equeals to one.


    def hanoi(self, n, source, helper, target): #This line is to define the variables that we need.
        print ("hanoi( ", n, source, helper, target, " called")
        if n > 0:
            self.hanoi(n - 1, source, target, helper) #This line is to move the tower of size n-1 to the helper.
            if source[0]:
                disk = source[0].pop() #This line is to move the disk from the source to the target.
                print ("moving " + str(disk) + " from " + source[1] + " to " + target[1]) #This line is to show the process.
                target[0].append(disk) #This line is to add the disk in the target.
            self.hanoi(n - 1, helper, source, target) #This line is to move the tower from the helper to the target.
        
    
    
    
    
    
    def FibonacciNumbers(self,n):
        if n == 0:
            return 0
        elif n== 1:
            return 1
        else:
            return self.FibonacciNumbers(self.n-1) + self.FibonacciNumbers(self.n-2) #This line is to call the function itself to calculate the next number.
        
        
        
r = recursivealgorithm() #This line is to define the class

#These three lines are to build the model of the hanoi.
source = ([4,3,2,1], "source") #This line is to show where the tower is.
target = ([], "target") #This line is to make an empty column.
helper = ([], "helper") #This line is to make an empty column.
r.hanoi(len(source[0]),source,helper,target) #This line is to execute the function hanoi.
print (source, helper, target)

r.factorial() #This line is to execute the function factorial.
r.FibonacciNumbers() #This line is to execute the function FibonacciNumbers.