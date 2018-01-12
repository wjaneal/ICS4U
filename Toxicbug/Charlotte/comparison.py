#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: chenquancheng
Date: Created on Fri Jan 12 12:54:02 2018
Title: comparison operators
Purpose: uses comparison operators and checks whether a letter is in a string
"""
#uses each comparison operator
x=input("Please input a number.") #lets the user input a number
y=input("Please input another number.") #lets the user input another number
xInteger=int(x) #converts the first number to an integer
yInteger=int(y) #converts the second number to an integer
#uses different comparison operators and prints different messages
if(xInteger==yInteger):
    print("x is equal to y")
else:
    print("x is not equal to y")
if(xInteger!=yInteger):
    print("x is not equal to y")
else:
    print("x is equal to y")
if(xInteger>yInteger):
    print("x is larger than y")
else:
    print("x is not larger than y")
if(xInteger>=yInteger):
    print("x is larger than or equal to y")
else:
    print("x is not larger than or equal to y")
if(xInteger<yInteger):
    print("x is less than y")
else:
    print("x is not less than y")
if(xInteger<=yInteger):
    print("x is less than or equal to y")
else:
    print("x is not less than or equal to y")
#checks whether certain letters('a','b','c','d','e') are in a string
string1=input("Please input a string.") #lets the user input a string
#checks whether 'a','b','c','d', and 'e' are in a string and prints different statements
if 'a' in string1:
    print("a is in the string!")
else:
    print("a is not in the string!")
if 'b' in string1:
    print("b is in the string!")
else:
    print("b is not in the string!")
if 'c' in string1:
    print("c is in the string!")
else:
    print("c is not in the string!")
if 'd' in string1:
    print("d is in the string!")
else:
    print("d is not in the string!")
if 'e' in string1:
    print("e is in the string!")
else:
    print("e is not in the string!")

#automatically checks whether each letter is in the string
string2=input("Please input a string.")
for lowerCase in range(97,123): #loops through lowercase letters
    if chr(lowerCase) in string2: #checks whether the lowercase letter is in the string
        print(chr(lowerCase)+" is in the string")
for upperCase in range(65,91): #loops through uppercase letters
    if chr(upperCase) in string2: #checks whether the uppercase letter is in the string
        print(chr(upperCase)+" is in the string")
'''
for letter in string2:
    if ((ord(letter)>=97 and ord(letter)<=122) or (ord(letter)>=65 and ord(letter)<=90)):
        print(letter+" is in the string!")
'''      