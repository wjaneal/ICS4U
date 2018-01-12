'''
Assignment 3 - Comparison Operators

Coding convention: 
(a) lower case file name
(b) Name, Date, Title, Purpose in multiline comment at the beginning
(c) mixedCase variable names

Reference for Operators:
https://www.tutorialspoint.com/python/python_basic_operators.htm


Write a program that does the following:
(a) Let the user input two numbers.
(b) Convert the numbers to integers
(c) In six if statements, compare the two numbers using the following operators: ==, !=, >, <, >=, <= and print out different messages whether each comparison is true or false.
(d) Let the user enter a string.
(e) Use 'in' statements to find out whether the letters 'a', 'b', 'c', 'd' or 'e' are in the string.  If yes, print a message to indicate this.
(f) Find a way to automatically check if each letter of the alphabet (upper or lower case) is in the string, printing a message if it is.
'''

a = 5 #Assignment operator: =  sets the value of a variable

#Comparison operators:
'''
a == 5 #Comparison operator: == checks whether the variable has a value
a > 5 # Greater than
a >= 5 # Greater than or equal to
a < 5 # Less than
a <= 5 #Less than or equal to
a != 5 #Not equal to
'''

#This is a function
def f(x): #x is the argument or parameter
    return 3*x + 4 #It returns a value based on x
print (f(9))

#Here is another function:
def checkLetter(letter, word):
    if letter in word:
    	return "The letter is in the word!"
    else:
    	return "The letter is not in the word!"

print(checkLetter('d', 'dog'))
print(checkLetter('d', 'apple'))







