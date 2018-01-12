'''
Assignment 3 - Typecasting

Coding convention: 
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


