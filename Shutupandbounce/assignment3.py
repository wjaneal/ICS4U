'''
Assignment 3 - Typecasting

Coding convention: 
(a) lower case file name
(b) Name: Emma, Date: Jan 12, Title: Assignment 3 - Typecasting,
Purpose:
(c) mixedCase variable names

Write a program that does the following:
(a) Let the user input two numbers.
(b) Convert the numbers to integers
(c) Use six comparison operators in six different if statements to compare the two numbers.  Print different outputs for true and false in each case.
(d) Let the user input a string
(e) Determine whether the letters 'a', 'b', 'c', 'd' or 'e' are in the string using five diffferent if statements.  Print appropriate output in each case.
(f) Find a way to check if each letter in the alphabet is in the string (upper and lower case) and print appropriate output. Use loops, comparison operators, decision structures and codes for the different letters of the alphabet.
'''
#(a) Let the user input two numbers and (b) convert the numbers to integers.
a = int(input("Enter a number:"))
b = int(input("Enter another one:"))
#(c) Use six comparison operators in six different if statements to compare the two numbers.
#Print different outputs for true and false in each case.
#> < >= <= == !=
if a>b:
    print("True")
else:
    print("False")
if a<b:
    print("True")
else:
    print("False")
if a>=b:
    print("True")
else:
    print("False")
if a<=b:
    print("True")
else:
    print("False")
if a==b:
    print("True")
else:
    print("False")
if a!=b:
    print("True")
else:
    print("False")
#(d) Let the user input a string
word = input("Enter a word:")
#(e) Determine whether the letters 'a', 'b', 'c', 'd' or 'e' are in the string using five diffferent if statements.  Print appropriate output in each case.
#(f) Find a way to check if each letter in the alphabet is in the string (upper and lower case) and print appropriate output.
#Use loops, comparison operators, decision structures and codes for the different letters of the alphabet.
def checkletter(word):
    list1 = ["a","b","c","d","e"]
    for i in range(0,len(list1)):
        if list1(i)in word:
            return("the letter",list1(i), " is in the word")
        else:
            return"not in"
print(checkletter(word))

