# -*- coding: utf-8 -*-
"""
Name: Xu, Yingjie (Mike)
Date: 2018-01-12
Program Title: assignment3
Purpose: 
(a) Let the user input two numbers.
(b) Convert the numbers to integers
(c) Use six comparison operators in six different if statements to compare the two numbers.  Print different outputs for true and false in each case.
(d) Let the user input a string
(e) Determine whether the letters 'a', 'b', 'c', 'd' or 'e' are in the string using five diffferent if statements.  Print appropriate output in each case.
(f) Find a way to check if each letter in the alphabet is in the string (upper and lower case) and print appropriate output. Use loops, comparison operators, decision structures and codes for the different letters of the alphabet
Variable names: i, j, a, b, str1, c
"""

i = eval(input('please give me a number: '))
j = eval(input('please give me another number: '))
a = int(i)
b = int(j)

print()

print ('The statement that '+str(a)+' is equal to '+str(b)+' is ',end='')
print (a==b)
print ('The statement that '+str(a)+' is less than '+str(b)+' is ',end='')
print (a<b)
print ('The statement that '+str(a)+' is greater than '+str(b)+' is ',end='')
print (a>b)
print ('The statement that '+str(a)+' is less than or equal to '+str(b)+' is ',end='')
print (a<=b)
print ('The statement that '+str(a)+' is greater than or equal to '+str(b)+' is ',end='')
print (a>=b)
print ('The statement that '+str(a)+' is not equal to '+str(b)+' is ',end='')
print (a!=b)

str1 = repr(input('Please input a string: '))
print()
print('part e')
if 'a' in str1:
    print ('a is in the '+str1)
if 'b' in str1:
    print ('b is in the '+str1) 
if 'c' in str1:
    print ('c is in the '+str1)
if 'd' in str1:
    print ('d is in the '+str1)
if 'e' in str1:
    print ('e is in the '+str1)    

print()
print('part f')
for c in range (65,123):
    if chr(c) in str1:
        print(str(chr(c))+' is in '+str1)
        
