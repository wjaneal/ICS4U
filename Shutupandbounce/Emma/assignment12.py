# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 01:35:50 2018
@author: fy
Assignment 12 - Recursive Algorithms - Towers of Hanoi
Purpose:To use recursive algorithms to solve problems.
 
Allow the user to choose any of the three functions and then interact with the function.  
The program should provide adequate instructions and output to be useful.
"""
#(1) Create a class with functions for three recursive algorithms:
#    factorials, the Towers of Hanoi and any other recursive function.  
class recursiveAlgorithms():
    def factorials(self,a):
        print('The number is',a)#Display the number being calculated.
        self.num = 1#Set an original value for the answer.
        while a >= 1:#As long as the number is greater than 1:
            self.num = self.num * a
            a = a - 1#The answer = a*(a-1)*(a-2)*...*1
        return self.num

    def hanoi(self,a, source, helper, target):#(how many disks(4),p1,p2,p3)
        print ("hanoi ",a, source, helper, target, " called")#Display the condition of Hanoi.
        if a > 0:
            # Move tower of size n - 1 to helper:
            self.hanoi(a - 1, source, target, helper)
            # Move disk from source peg to target peg
            if source[0]:
                disk = source[0].pop()#Put the biggest disk to the last term.
                #State that moving the biggest on from the top of the source to the top of the target.
                print ("moving " + str(disk) + " from " + source[1] + " to " + target[1])
                target[0].append(disk)#Add the disk to the target peg.
            # Move tower of size n-1 from helper to target
            self.hanoi(a - 1, helper, source, target)
        source = ([len(a)], 'in the source')
        target = ([], 'in the target')
        helper = ([], 'in the helper')
        print(source, helper, target)  
        self.hanoi(len(source[0]),source,helper,target)#Run the Hanoi program.

    
    def Fibonacci(self,a): #Function for calculating the Fibonacci sequence.
        if a == 1 or a == 2: #The first and second item in the Fibonacci sequence is 1.
            return 1
        if a > 2:
            return self.Fibonacci(a-1)+self.Fibonacci(a-2) #Each number (starting from the third item) is the sum of the two preceding numbers.

    def interactions(self):
        self.quit = False#Keep the progam working.
        while(self.quit == False):#As long as the program is working:
            #Ask the user to enter numbers or to quit.
            a = int(input("Hello player. Here are several calculations will be shown to you. Pick a number:(Enter '0' to quit)"))
            if a ==0:
                break#Stop the program by entering 'q'.
            print('The factorial of',str(a),' is',str(self.factorials(a)))#Display the answer.
            print("Here are the first",str(a),"terms of the Fibonacci sequence:")
            for i in range(1,a+1):#Ranging from 1 to the next term after the one the user chooses:
                print(self.Fibonacci(i))#Display the Fibonacci sequence by terms.
            
run = recursiveAlgorithms()#Create an instance of the class.
run.interactions()#Run the program.