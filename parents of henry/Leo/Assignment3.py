#!/usr/bin/env python3

# -*- coding: utf-8 -*-

'''
Name: Leo Shen <szclsya@gmail.com>
Date: 2018-01-10
Program Title: NumLoop
Purpose: Loop though 1000 number and search for numbers which are divisible by 3 or 19.
'''

print("PLease input number 1:")
num1 = int(float(input()))
print("Please input number 2:")
num2 = int(float(input()))
print("Please input a string:")
string = str(input())

if num1 == num2:
    print("Number 1 is as big as number 2")
if num1 != num2:
    print("Number 1 is unequal to number 2")
if num1 > num2:
    print("Number 1 is bigger than bumber 2")
if num1 < num2:
    print("Number 1 is smaller than number 2")
if num1 <= num2:
    print("Number 1 is smaller or as big as number 2")
if num1 >= num2:
    print("Number 1 is bigger or as big as number 2")

for i in range (65,123):
    if chr(i) in string:
        print("Character "+chr(i)+" is in the string")
