
#Assignment 2 - Typecasting

'''
Mandy,Jan 11,Assignment2:Typecasting
Purpose:
Write a program that does the following:
(a) Let the user input two numbers.
(b) Convert the numbers to integers
(c) Print the sum, difference, product and quotient of the numbers.
(d) Repeat (b) and (c) for floating point
(e) Convert the numbers to strings.
(f) Output the four results as strings as follows: The sum of a and b is 5.667, etc. for subtraction, multiplication and division.
'''
a = int(input("Please put an integer!"))
b = int(input("Please put an integer!"))
print ("The sum of a and b", a+b)
print ("The difference of a and b", a-b)
print ("The product of a and b", a*b)
print ("The quotient of a and b", a/b)


c = float(input("Please put an floating point number!"))
d = float(input("Please put a floating point number!"))
e = c + d
f = c - d
g = c*d
h = c/d

print ("The sum of c and d", str(e))
print ("The difference of c and d", str(f))
print ("The product of c and d", str(g))
print ("The quotient of c and d", str(h))
