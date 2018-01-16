# -*- coding: utf-8 -*-
"""
Name: Song, Jiwei (Mark)
Date: 2018-01-11
Program Title: Print numbers
Purpose:
(a) Let the user input two numbers.
(b) Convert the numbers to integers
(c) Print the sum, difference, product and quotient of the numbers.
(d) Repeat (b) and (c) for floating point
(e) Convert the numbers to strings.
(f) Output the four results as strings as follows: The sum of a and b is 5.667, etc. for subtraction, multiplication and division.
Variable name: 
"""

a = eval(input('please input the first number: '))
b = eval(input('please input the second number: '))

print()

inta = int(a)
intb = int(b)
print('the sum of the two numbers =', inta + intb)
print('the difference of the two numbers =', inta - intb)
print('the product of the two numbers =', inta * intb)
print('the quotient of the two numbers =', inta / intb)

print()

floata = float(a)
floatb = float(b)
print('the sum of the two numbers =', floata + floatb)
print('the difference of the two numbers =', floata - floatb)
print('the product of the two numbers =', floata * floatb)
print('the quotient of the two numbers =', floata / floatb)

print()

print('the sum of '+str(a)+' and '+str(b)+ ' is equal to '+str(floata + floatb))
print('the difference of '+str(a)+' and '+str(b)+ ' is equal to '+str(floata - floatb))
print('the product of '+str(a)+' and '+str(b)+ ' is equal to '+str(floata * floatb))
print('the quotient of '+str(a)+' and '+str(b)+ ' is equal to '+str(floata / floatb))


