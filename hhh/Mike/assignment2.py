# -*- coding: utf-8 -*-
"""
Name: Xu, Yingjie (Mike)
Date: 2018-01-11
Program Title: print numbers
Purpose: 
(a) Let the user input two numbers.
(b) Convert the numbers to integers
(c) Print the sum, difference, product and quotient of the numbers.
(d) Repeat (b) and (c) for floating point
(e) Convert the numbers to strings.
(f) Output the four results as strings as follows: The sum of a and b is 5.667, etc. for subtraction, multiplication and division.
Variable names: a, b, inta, intb, floata, floatb
"""

a = eval(input('please input the first number: '))
b = eval(input('please input the second number: '))

print()
print('For this section, print as integers:')
inta = int(a)
intb = int(b)
print ('the sum of two numbers =', inta + intb)
print ('the difference of two numbers =', inta - intb)
print ('the product of two numbers =', inta * intb)
print ('the quotient of two numbers =', inta / intb)

print()
print('For this section, print as floating point numbers:')
floata = float(a)
floatb = float(b)
print ('the sum of two numbers =', floata + floatb)
print ('the difference of two numbers =', floata - floatb)
print ('the product of two numbers =', floata * floatb)
print ('the quotient of two numbers =', floata / floatb)

print()
print('For this section, print as strings:')
print('sum of '+str(a)+' and '+str(b)+' is equal to '+str(floata + floatb))
print('difference of '+str(a)+' and '+str(b)+' is equal to '+str(floata - floatb))
print('product of '+str(a)+' and '+str(b)+' is equal to '+str(floata * floatb))
print('quotient of '+str(a)+' and '+str(b)+' is equal to '+str(floata / floatb))
