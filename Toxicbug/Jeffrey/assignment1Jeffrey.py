"""
Author: Jeffrey 
Date: 10th January 2018
Title: division
Function: Loop through 1000 numbers, and find the numbers that are divisible by 3 or 19.
"""

#loop from 0 to 1000:
for number in range(0,1000):
    if number%3 == 0: #find the number that is divisible by 3
        print(number, "is divisible by 3.")
    elif number%19 == 0: #find the number that is divisible by 19
        print(number, "is multiple of 19.")
      