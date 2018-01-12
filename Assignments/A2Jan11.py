'''
Assignment 2 - Typecasting

Coding convention: 
(a) lower case file name
(b) Name, Date, Title, Purpose in multiline comment at the beginning
(c) mixedCase variable names

Reference for Typecasting: 
https://www.tutorialspoint.com/python/python_variable_types.htm


Write a program that does the following:
(a) Let the user input two numbers.
(b) Convert the numbers to integers
(c) Print the sum, difference, product and quotient of the numbers.
(d) Repeat (b) and (c) for floating point
(e) Convert the numbers to strings.
(f) Output the four results as strings as follows: The sum of a and b is 5.667, etc. for subtraction, multiplication and division.


'''

#Type casting
x = 5  #This is an integer
y = 6  #This is also an integer
a = 5.0 #This is a floating point number
b = 6.0 #This is too

xstring = str(x) #Typecast x into a string
print("The length of the side is "+xstring)

print(x/y)
print(a/b)
print(x/y+a/b)
print (int(a/b)) #This converts the number back to an integer



