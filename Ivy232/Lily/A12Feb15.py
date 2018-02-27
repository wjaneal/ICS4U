'''
Assignment 12 - Recursive Algorithms - Towers of Hanoi


Coding convention: 
(a) lower case file name
(b) Lily, 25 Feb.2018, Recursive Algorithms
(c) mixedCase variable names
Purpose:
(1) Create a class with functions for three recursive algorithms.  
(2)Include factorials, the Towers of Hanoi and any other recursive function.  
(3)Allow the user to choose any of the three functions and then interact with the function.  
(4)The program should provide adequate instructions and output to be useful.
'''


from turtle import *

class Recur:
    def func1(self,x): #This is for the game about factorial
        if x == 1: #define a number when x = 1, allowing the function to recur.
            return 1 #THis is to provide the key unknown variable in the end.
        else:
            return x * self.func1(x-1) #This is to calculate the factorial.
        
    def tower(self, N, Beg, Aux, End): #This is for the game about Towers of Hanoi.
        if N == 1: #This is to move the botton tower to the "pole of End" after moving the other to the "pole of Auxiliary".
            print(Beg + " –> " + End) #This is to print out the step taken.
        else:
            self.tower(N-1,Beg, End, Aux) #This is to print all the steps taken before there is only one botton tower left in the "pole of Beginning".
            self.tower(1,Beg, Aux, End) #This is to move the botton tower to the "pole of End" after moving the other to the "pole of Auxiliary".
            self.tower(N-1, Aux, Beg, End) #This is to move all of the towers except for the botton one to the "pole of End".

    def func3(self,length, depth): #This is the function of drawing a snowflake.
        if depth == 0:
            forward(length) #This is to go forward for 1 unit
        else:
            self.func3(length/3, depth-1) #This is the start of the loop.
            right(60) #This step is to make a turn and also connect the end of every loop.
            self.func3(length/3, depth-1) #second loop
            left(120) #This step is to make a turn and also connect the end of every loop.
            self.func3(length/3, depth-1) #third loop
            right(60) #This step is to make a turn and also connect the end of every loop.
            self.func3(length/3, depth-1) #forth loop

        
        
    def func3_(self,length,repeat,spe):
        speed(spe) #This is to define a speed for Turtle.
        for i in range(3): #There are mainly three parts in a flake
            self.func3(length,repeat) #This is to call the function "func3" to draw the three sides of a complete snowflake. (We know the prototype of a snowflake is a triangle with three sides.)
            left(120) #This is to make a turn when a loop of function "func3" is finished.
        #if input("Do you want to quit the snowflake?") == "yes":
        bye() #This is to quit this snowflake-drawing-game.
            
    def control(self): #Create a function for the initiation of the whole game.
        self.playGame = True # This is to create a condition for the initiation of the game.
        while (self.playGame == True): #This is to make orders when the prerequisite is met.
            print("There are three games available:<A> for Factorials; <B> for Towers of Hanoi; <C> for Drawing a snowflake ")
            print("")
            print("You can also type in <E> to quit the games.")
            print("")
            choi=input("Please type in the one you would like to play:") #This is to require the player to make a choice.
            if choi == "A": #This is to direct the player to certain type of game.
                number = int(input("For what number do you want to figure out the factorial?"))
                print("The factorial of " + str(number) + " is " + str(self.func1(number)))
            if choi == "B": #This is to direct the player to certain type of game.
                number = int(input("How many towers do you want for the Towers of Hanoi?"))
                print("")
                print("The towers should be moved like below:")
                print("")
                print("(attention: A, B and C below represents 3 Poles)")
                self.tower(number, "A", "B", "C") #This is to print out the way the towers are moved.
            if choi == "C": #This is to direct the player to certain type of game.
                length = int(input("What length of the six sides do you want for the snowflake?(Please enter a number big enough)"))
                repeat= int(input("How many times of divergence do you want for the snowflake?(Please do not enter a number more than 5)"))
                spe = int(input("What drawing speed do you want for the snowflake?"))
                self.func3_(length, repeat, spe)
            if choi == "E": #This is to provide the player a choice to quit the whole game when they want to.
                self.playGame = False #This is to cancel the base of the whole game when the player chooses to quit.
            else: 
                continue #This is to keep the game working when the player wants to continue
                
            
start = Recur() #This is to create a instance for the class.
start.control() #This is to call the function in the class with the instance.







 

























































'''
=======
>>>>>>> 81e8aa76a02d1c71b464c2e0e4b35300b428e514
'''
