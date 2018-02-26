# -*- coding: utf-8 -*-
"""
Name: Song, Jiwei(Mark)
Date: 2018-02-24
Program Title: Recursive Algorithms
Purpose: 
(1) Create a class with functions for three recursive algorithms.  
(2)Include factorials, the Towers of Hanoi and any other recursive function.  
(3)Allow the user to choose any of the three functions and then interact with the function.  
(4)The program should provide adequate instructions and output to be useful.
"""

class recursive():#This is to create a class
    def Factorial(self):#This defines a function
        if self==1:#This sets the fundamental procedure
            return 1#This is used to return the value
        else:
            return self*recursive.Factorial(self-1)#This returns other values
    
    def Hanoi(self,a='A',b='B',c='C'):#This defines the function for Hanoi tower
        if self == 1:#This is used to set the fundamental operation
            print('move '+str(self)+'from '+a+'to '+c)#This is to move a disk to another place
        
        else:
            recursive.Hanoi(self-1,a,c,b)#This is used to move away all the disks that are on the biggest disk

            print('move '+str(self)+'from '+a+'to '+c)#This is to move the biggest disk away

            recursive.Hanoi(self-1,b,a,c)#This is to move the disks back on the biggest disk
    
    def Fibonacci(self):#This defines a function of Fibonacci
        if self == 1 or self==2:#This is to used to set the basic two values
            return 1#This is to return value
        else:
            return recursive.Fibonacci(self-1)+recursive.Fibonacci(self-2)#This returns the value besides adds the former two numbers together
        
    def act():
        a = True#This is used to set the Keepgoing variable to decide whether the programme should keep going
        while a is True:#This is used to start a loop
            #This is to know what the user want to do
            N= int(input('which function do you want to use? input 1 for factorial,2 for tower of Hanoi and 3 for Fabonacci sequence. If you want to exit, input 4'))
            if N == 1:#This is used to activate the factoial part
                #This is used to show instruction and get the number used in factorial function
                N1 = int(input('for factorial, input the number and I will give you the factorial of it as output'))
                #This is used to show the output
                print('the fatorial of '+str(N1)+' is',recursive.Factorial(N1))
                
            if N==2:#This is to activate the tower of Hanoi function
                print('The numbers represent the size of the disk and A,B,C indicates stacks')#This is to show how the instructions work

                #This is to show instruction and get the number of disks
                N2 = int(input('for tower of Hanoi, input the number of disks and follow my instruction'))
                #This is to operate and show the instructions
                recursive.Hanoi(N2)
                
            if N==3:#This is to active the Fabonacci sequence function
                N3 = int(input('for Fibonacci sequence, input the number(N) and I will give you the corresponding element in Fibonacci sequence of N(the Nth number in the sequence)'))
                #This is to show the output
                print(recursive.Fibonacci(N3))
                
            if N == 4:#This is to stop the loop
                a = False

                #This is to active the programme
recursive.act()