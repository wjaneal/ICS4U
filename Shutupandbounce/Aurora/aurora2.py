ucn#(a)assignment2
"""
Write a program that does the following:
(a) Let the user input two numbers.
(b) Convert the numbers to integers
(c) Print the sum, difference, product and quotient of the numbers.
(d) Repeat (b) and (c) for floating point
(e) Convert the numbers to strings.
(f) Output the four results as strings as follows: The sum of a and b is 5.667, etc. for subtraction, multiplication and division.
"""
# 2018/01/11,Aurora Hou
#mixedCase variable names

woW = (input("please input a number:  "))
xxX = (input("please input another number:  "))
woW = int(woW)
xxX = int(xxX)
print(woW + xxX)
print(woW - xxX)
print(woW * xxX)
print(woW / xxX)
woW = float(woW)
xxX = float(xxX)
print(woW + xxX)
print(woW - xxX)
print(woW * xxX)
print(woW / xxX)
string1 = str(woW + xxX)
string2 = str(woW - xxX)
string3 = str(woW * xxX)
string4 = str(woW / xxX)
print("The sum of two numbers is "+string1+".")
print("The difference of two numbers is "+string2+".")
print("The product of two numbers is "+string3+".")
print("The quotient of two numbers is "+string4+".")
