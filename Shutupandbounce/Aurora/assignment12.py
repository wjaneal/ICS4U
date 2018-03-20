'''
Assignment 12 - Recursive Algorithms - Towers of Hanoi
Coding convention: 
(a) lower case file name
(b) Name, Date, Title, Purpose in multiline comment at the beginning
(c) mixedCase variable names
(1) Create a class with functions for three recursive algorithms.  Include factorials, the Towers of Hanoi and any other recursive function.  Allow the user to choose any of the three functions and then interact with the function.  The program should provide adequate instructions and output to be useful.
'''
#import sys
#sys.setrecursionlimit(10000000)

class Recursive():
    def Factorials(self,a):
        self.a = a
        if self.a == 1 :
            return 1   
        else:
            self.fa = self.a * self.Factorials(self.a - 1)  
            return self.fa
        
    def Hanoi(self,a,A,B,C):
        self.a = a
        self.A = A
        self.B = B
        self.C = C
        if (self.a == 1) :
            print("Moving ", self.A," ",self.C) #when there is only one plate,move it from A pillar to C pillar
        else:
            self.Hanoi(self.a - 1, self.A, self.C, self.B)  #move the left n-1 plates on the A pillar to the B pillar within the help of C pillar
            print("Moving ", self.A," ",self.C) #move the last plate on A pillar directly to the C pillar
            self.Hanoi(self.a - 1, self.B, self.A, self.C) 
            
    def Fibonacci(self,n):
        if self.n==0:
            return 0
        elif self.n==1:
            return 1
        else:
            return Fibonacci(self.n-1) + Fibonacci(self.n-2)
        
    def Application(self):
        self.choice = input("Which recursive algorithm you want to use?\n F.Factorial \n H.Hanoi \n Fi.Fibonacci")
        if self.choice == 'F':
            self.a = input("The number is :\n")
            print("The factorial of ",int(self.a)," is ",self.a,".")
        if self.choice == 'H':
            self.a = input("How many plates there are?:\n")                                                                                     
            print("Three pillars from left to right are A  B  C")
            print("Here is the steps:\n",self.Hanoi(self.a,A[0],B[1],C[2])) #This prints the steps of moving the disks. 
        if self.choice == 'Fi':                                                                                                                                          
            self.n = int(input("The number of terms is :\n"))
            for self.i in range(1,self.n+1):
                print(self.Fibonacci(self.i))

R = Recursive()
R.Factorials(10)
R.Hanoi(5,1,2,3)
R.Fibonacci()
R.Application()