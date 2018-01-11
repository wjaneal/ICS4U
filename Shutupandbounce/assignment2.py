'''
Assignment 2 - Typecasting
Name: Emma
Title: Assignment for Typecasting
Purpose:to write a program that converts different types of data.
mixedCase variable names:answer1,answer2,s,d,p,q

Write a program that does the following:
(a) Let the user input two numbers.
(b) Convert the numbers to integers
(c) Print the sum, difference, product and quotient of the numbers.
(d) Repeat (b) and (c) for floating point
(e) Convert the numbers to strings.
(f) Output the four results as strings as follows: The sum of a and b is 5.667, etc. for subtraction, multiplication and division.

'''
answer1 = int(input("Plz enter the first of two integers:"))#Let the user input two numbers.
answer2 = int(input("Plz enter the second of two integers:"))


s=answer1+answer2
d=answer1-answer2
p=answer1*answer2
q=answer1/answer2
#Convert the numbers to integers.
s = int(s)
d = int(d)
p = int(p)
q = int(q)
   
#Print the sum, difference, product and quotient of the numbers.
print(s,d,p,q)

#Convert the numbers to floating point numbers.
s = float(s)
d = float(d)
p = float(p)
q = float(q)
#Print the sum, difference, product and quotient of the numbers again.
print(s,d,p,q)
#Output the four results by Converting the numbers to strings.
print("The sum of two numbers is", str(s))
print("The difference of two numbers is", str(d))
print("The product of two numbers is", str(p))
print("The quotient of two numbers is", str(q))

