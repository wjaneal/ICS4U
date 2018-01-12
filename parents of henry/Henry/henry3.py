# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Name:Henry
Date: 12/Tan/2018
Program Title: Type casting
Purpose:
(a) lower case file name
(b) Name, Date, Title, Purpose in multiline comment at the beginning
(c) mixedCase variable names

Write a program that does the following:
(a) Let the user input two numbers.
(b) Convert the numbers to integers
(c) Use six comparison operators in six different if statements to compare the two numbers.  Print different outputs for true and false in each case.
(d) Let the user input a string
(e) Determine whether the letters 'a', 'b', 'c', 'd' or 'e' are in the string using five diffferent if statements.  Print appropriate output in each case.
(f) Find a way to check if each letter in the alphabet is in the string (upper and lower case) and print appropriate output. Use loops, comparison operators, decision structures and codes for the different letters of the alphabet.


"""
a = eval(input ('give me a number:'))
b = eval(input ('give me another number:'))
Int1 = int(a)
Int2 = int(b)


if Int1 == Int2 :
    print (str(Int1)+" is equal to "+str(Int2) )

if Int1 >= Int2:
    print (str(Int1)+" is greater than or equal to "+str(Int2) )

if Int1 <= Int2:
    print (str(Int1)+" is less than or equal to  "+str(Int2) )
    
if Int1 > Int2:
    print (str(Int1)+" is greater than  "+str(Int2) )

if Int1 < Int2:
        print (str(Int1)+" is less than  "+str(Int2) )

if Int1 != Int2:
    print (str(Int1)+" is not equal to  "+str(Int2) )
    
String = input('give me a string:') 
for i in range (65,123):
    if chr(i) in String:
        print(chr(i) ,' is in ', String)







    
    
