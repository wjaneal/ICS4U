'''
Name: Emma
Date: Jan. 10, 2017
Title of program: Assignment 1
Purpose of program: Loop through 1000 number.
                     If the number is divisible by 3, print"divisible by 3".
                     If the number is divisible by 19, print"multiple by 19". 
Variable name:i
'''
#There is a for loop.
for i in range(1,1001):
    if i % 3 ==0:
        print(i, "is divisible by 3.")
    elif i % 19 ==0:
        print(i, "is the multiple of 19.")
    else:
        print(i)
    
