# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 01:37:09 2018

@author: 11256
"""
'''
Create a class with functions for three recursive algorithms. 
 Include factorials, the Towers of Hanoi and any other recursive function. 
 Allow the user to choose any of the three functions and then interact with the function. 
 The program should provide adequate instructions and output to be useful.
 '''
 
class recursive():
    def factorial(self,n):
        #define the factorial algorithm
        if n == 1:
            return 1
        # the factorial of 1 is 1
        else:
            return n * self.factorial(n-1)
        #calculate factorial of other number
        
    def hanoi(self,n, from_tower, to_tower, using_tower):
        #define the haoi algorithm, n is the stick
        if n > 0:
            self.hanoi(n-1, from_tower, using_tower, to_tower)
            print ('move disk from ', from_tower, ' to ', to_tower)
            #move the disk from the other
            self.hanoi(n-1, using_tower, to_tower, from_tower)
            
    def FibonacciNumbers(self,n):
        #define the fibonacciNumber
        if n == 0:
            return 0
        #the fibonaccinumber of 0 is 0
        elif n== 1:
            return 1
        ##the fibonaccinumber of 1 is 1
        else:
            return self.FibonacciNumbers(n-1) + self.FibonacciNumbers(n-2)

r = recursive()
print(r.factorial(10))
#excute the factorial funcrion
r.hanoi(3, 'A', 'B', 'C')
#excute the hanoi function
print(r.FibonacciNumbers(10))
#excute the finbonanumber function
