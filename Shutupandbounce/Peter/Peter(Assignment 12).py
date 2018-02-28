#Assignment 12 - Recursive Algorithms - Towers of Hanoi
#Name:Peter Zeng
#Date: February,15 2018
#Program Title:Towers of Hanoi
#Program Function:
##(1) Create a class with functions for three recursive algorithms.
#Include factorials, the Towers of Hanoi and any other recursive function.
#Allow the user to choose any of the three functions and then interact with the function.
#The program should provide adequate instructions and output to be useful.
import datetime

i = datetime.datetime.now()
print("Time: %s/%s/%s %s:%s:%s" % (i.day,i.month,i.year,i.hour,i.minute,i.second))
class recursive:
    def hanoi(self,p,a,b,c):  #a kind of mathmatical games for moving the tray
        if p == 1:    #
            print("Move", a ,"  -->  ", b) 
            return   # end it up
        self.Hanoi(p-1, a , b , c) 
        print ("Move", a ," -->   ",c)
        self.Hanoi(p-1, b , a , c)
        print ("Move", b ,"-->  ",c)
        
    def factorials(self,num,p):
        num = 1 # set a num
        while p >= 1:
            num = num * p #time p when there's a chosen number
            p = p - 1  #it is the same as formulp*(p-1)*(p-2)......
            return num #end it up
        
    def sum_number(self,p):
        if p <= 0: 
            return 0
        return p + self.sum_number(p-1)
        
    def gameplaytime(self):
        print("Hello,welcome to my math zone!")
        self.fun = False
        while(self.fun == False):
            print("what's your choice for the best you like below?")
            print("put f,you will get factorials")
            print("put s,you will get sum_number")
            print("put h,you will get Hanoi tower")
            print("put q,you will get out of my programme")
            i = input("put your letter here(I notice you above):")
            if i == 'f':
                print("Welcome to factorials zone,quick to put a number,I can't wait for this!Remember the math formula x*(x+1)....")
                self.a = input("which number you prefer?put it here:")
                print("the result is shown here: ", str(self.factorials(num,p)))
            if i == 's':
                print("Welcome to sum_number zone,quick to put a number,I can't wait for this!do your sum up now!")
                self.b = input("which number you prefer to add?put it here:")
                print("the result is shown here: ", str(self.sum_number(p)))
            if i == 'h':
                print("Welcome to Hanoi zone,quick to put a number,I can't wait for this!put the favourite number for seeing the movement!\nthere have 3 different types of disks.A,B and C")
                self.c = input("guess a number to see how it goes: ")
                print("here is the result here:", str(self.hanoi(a,b,c)))

            if i == 'q':    #quit the game
                self.fun = True
            else:
                continue
r = recursive()
r.gameplaytime()
r.sum_number()
r.factorials()
r.hanoi()


                