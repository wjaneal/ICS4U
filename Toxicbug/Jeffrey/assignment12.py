# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 14:37:31 2018

@author: Jeffrey

purpose:
Create a class with functions for three recursive algorithms.  Include factorials, the Towers of Hanoi and any other recursive function. 
Allow the user to choose any of the three functions and then interact with the function.  
The program should provide adequate instructions and output to be useful.
"""

class recursiveAlgorithms:
    
    def factorials(self, n): # a function that runs factorial
        #self.n = int(input("What number are you going to be testing by factorial?")) # prompt the user to input a number
        if n == 0: #base case is when n = 0, return 1
            return 1
        else: # when the number is greater than 1, recurve the function
            return n*self.factorials(n-1) #return the result

    def hanoi(self,N,ini,mid,end): # this is a function that runs the tower of hanoi game
        if N == 1: # if there is only one disk, then put that from initial to the end
            print(ini, "to" , end)
        else:
            self.hanoi(N-1,ini,end,mid) # Move top (N-1) disks from initial to middle 
            self.hanoi(1,ini,mid,end) # Move top 1 disks from initial to end 
            self.hanoi(N-1,mid,ini,end) # Move top (N-1) disks from middle to end

    def sum_digits(self, a): # this is a function that can get the sum of all the digits of a number
        # when the digit is smaller than 10, then just return the number itself
        if a < 10: 
            return a
        # if the number is greater then 10, then we need to add up all the digits
        else:
            all_but_last, last = a // 10, a % 10 #devide the whole number into two parts, one part is the last digit, another one is all the digits apart from the last digit
            a = self.sum_digits(all_but_last) + last #add up those two part and recurve if necessary
            return a # return the final value
        
    def play(self): # let the user actually play this game
        self.end = False # set end the game initially to false
        print("\nWelcome to my litte program, choose a game to play, mate!") # a welcome sentence
        while self.end == False: # keep playing while not ending the game
            #instruct users about key features
            print("\nType F if you want to play factorial function")
            print("\nType H if you want to play tower of hanoi")
            print("\nType S if you want to know the sum of a long number of its digits")
            print("\nType E if you want to end this game")
            k = input("You may type here: ") # ask for a command
            if k == 'F': # start factorial function
                print("\nWelcome, in this part, you can know the factorial of a number immidiately")
                n = int(input("\nWhat number would you want to be tested? "))
                print("\nThe result would be: ", str(self.factorials(n)))
            if k == 'H': # start the Hanoi function
                print("\nWelcome to the Tower of Hanoi game, in this part, you can immidiately know all the steps to solve a tower of hanoi game")
                print("\nLets assume the three pegs are A, B and C individually, in which A is the initial one, B is the middle one and C is the final one")
                N = int(input("\nHow many disks do you have to solve: "))
                print("\nHere is what you need to do: ")
                self.hanoi(N,"A","B","C")
            if k == 'S': # start the sum of digits function 
                print("\nIn this part, you can know the sum digits of a very long number immediately I promise")
                a = int(input("\nYou can input your number here: "))
                print("\nThe result would be: ", str(self.sum_digits(a)))
            if k == 'E': # end this program
                print("\nSee you next time!")
                self.end = True
            else:
                continue
                
#initialize the program          
a = recursiveAlgorithms()
a.play()














