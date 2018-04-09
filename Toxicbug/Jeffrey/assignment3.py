# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 12:49:20 2018

@author: Jeffrey
"""

# Let users input 2 numbers
while True:
    try:
        a = int(input("please input the first number "))
        b = int(input("please input the second number "))
        break
    except ValueError:
        print("It must be a number")

#make comparisons 
if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")
if a > b:
    print("a is greater than b")
if a < b:
    print("a is smaller than b")

#Check whether certain letters are in a string
string1 = input("please input a string")
if 'a' in string1:
    print("a is in the string")
else:
    print("a is not in the string")
if 'b' in string1:
    print("b is in the string")
else:
    print("b is not in the string")
if 'c' in string1:
    print("c is in the string")
else:
    print("c is not in the string")
if 'd' in string1:
    print("d is in the string")
else:
    print("d is not in the string")
if 'e' in string1:
    print("e is in the string")
else:
    print("e is not in the string")

# Automatically check whether each letter is in the string
for i in range(97,123):
    if chr(i) in string1:
        print(chr(i), " is in the string")
for ii in range(65,91):
    if chr(ii) in string1:
        print(chr(ii), " is in the string")



