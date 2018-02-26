# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 14:37:31 2018

@author: Jeffrey

purpose:
Create a class with functions for three recursive algorithms.  Include factorials, the Towers of Hanoi and any other recursive function.  Allow the user to choose any of the three functions and then interact with the function.  
The program should provide adequate instructions and output to be useful.
"""

class recursiveAlgorithms:
    
    def factorials(self):
        self.n = int(input("What number are you going to be testing by factorial?"))
        if self.n == 0: #base case
            return 1
        else:
            self.returnNumber = self.n * self.factorial( self.n - 1 )  # recursive call
            return self.returnNumber
        
    def tower(self):
        pass
    
    def anotherOne(self):
        pass
    
    def play(self):
        pass
    
