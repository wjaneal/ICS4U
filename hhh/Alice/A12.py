#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 21:28:53 2018
Create a class with functions for three recursive algorithms. 
Include factorials, the Towers of Hanoi and any other recursive function. 
Allow the user to choose any of the three functions and then interact with the function.  
The program should provide adequate instructions and output to be useful.
@author: haichunkan
"""

class recursivealgorithm():
    def factorial(n):#n*(n-1)*(n-2)*(n-3)
        if n == 0:
            return 1 
        else:
<<<<<<< HEAD
            return n * recursivealgorithm.factorial(n-1) #recure until n=0
    def moveTower(h,FP, TP, HP):#height,from pole,to pole,helpingpole
        if h >= 1:
            recursivealgorithm.moveTower(h-1,FP,HP,TP)#Move a tower of height-1 to an intermediate pole, using the final pole.
            print("moving disk from",FP,"to",TP)#Move the remaining disk to the final pole.
            recursivealgorithm.moveTower(h-1,HP,TP,FP)#Move the tower of height-1 from the intermediate pole to the final pole using the original pole.
    def fibonacci(n):#note that 0 is the 0 item in fibonacci
        if n == 0:
            return 0 
        if n == 1:
            return 1 
        else:
            return recursivealgorithm.fibonacci(n-2) + recursivealgorithm.fibonacci(n-1) #start from the 3rd number, it = sum of the 2 numbers before it
    def sumOfAllDigits(n):#calculate sum of all digits in a number
        if n < 10:
            return n #the sum is itself if n<10
        else:
            notlast=n // 10 
            last = n % 10
            return recursivealgorithm.sumOfAllDigits(notlast) + last 	#seperate the digits
    def initiation():
        print("input f for factoial")
        print("input M for moveTower")
        print("input F for fibonacci")
        print("input S for sumofdigits")
        print("input E for esc")
        ini="init"
        while ini != "E":
            ini=input("choose: ")
            if ini == "f":
                c="Y"
                while c != "N" :
                    n=int(input("multiply integer up to: "))
                    print(recursivealgorithm.factorial(n))#start factorial funtion
                    c=input("Continue? Y for yes, N for no: ")
            elif ini == "M":
                c="Y"
                while c != "N" :
                    h=int(input("move tower of disk: "))#start movetower funtion
                    recursivealgorithm.moveTower(h,"origin pole","final pole","helping pole")
                    c=input("Continue? Y for yes, N for no: ")
            elif ini == "F":
                c="Y"
                while c != "N" :
                    n=int(input("which item in fabonacci sequence: "))
                    print(recursivealgorithm.fibonacci(n))#start fibonacci function
                    c=input("Continue? Y for yes, N for no: ")        
            elif ini == "S":
                c="Y"
                while c != "N" :
                    n=int(input("sum of all digits in integer: "))
                    print(recursivealgorithm.sumOfAllDigits(n))#start sumdigits funtion
                    c=input("Continue? Y for yes, N for no: ")        
            else:
                return()#exit
recursivealgorithm.initiation()
                
=======
            return()
initiation()
#print(factorial(2))                
>>>>>>> 8472a78b812ea6d188a698f39120c3f4c0a20492
