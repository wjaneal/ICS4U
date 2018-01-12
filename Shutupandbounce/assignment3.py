'''
Assignment 3 - Typecasting

Coding convention: 
(a) lower case file name
(b) Name: Emma, Date: Jan 12, Title: Assignment 3 - Typecasting,
<<<<<<< HEAD
Purpose:
(c) mixedCase variable names

Write a program that does the following:
(a) Let the user input two numbers.
(b) Convert the numbers to integers
(c) Use six comparison operators in six different if statements to compare the two numbers.  Print different outputs for true and false in each case.
(d) Let the user input a string
(e) Determine whether the letters 'a', 'b', 'c', 'd' or 'e' are in the string using five diffferent if statements.  Print appropriate output in each case.
(f) Find a way to check if each letter in the alphabet is in the string (upper and lower case) and print appropriate output. Use loops, comparison operators, decision structures and codes for the different letters of the alphabet.
=======
Purpose:To use comparison operators to solve problem and check whether a letter is in a word.
(c) mixedCase variable names:a, b, u, l, word 
>>>>>>> c65b72842c94ac3d74cf98e6207d6106d0927b6d
'''
#(a) Let the user input two numbers and (b) convert the numbers to integers.
a = int(input("Enter a number:"))
b = int(input("Enter another one:"))
#(c) Use six comparison operators in six different if statements to compare the two numbers.
#Print different outputs for true and false in each case.
#> < >= <= == !=
if a>b:
<<<<<<< HEAD
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

=======
    print(a,">",b)
else:
    print(a,"is not greater than",b)
if a<b:
    print(a,"<",b)
else:
    print(a,"is not smaller than",b)
if a>=b:
    print(a,"is greater than or equal to",b)
else:
    print(a,"is not greater than or equal to",b)
if a<=b:
    print(a,"is smaller than or equal to",b)
else:
    print(a,"is not smaller than or equal to",b)
if a==b:
    print(a,"is equal to",b)
else:
    print(a,"is not equal to",b)
if a!=b:
    print(a,"is not equal to",b)
else:
    print(a,"is equal to",b)
#(d) Let the user input a string
word = input("Enter a word:")
#(e) Determine whether the letters 'a', 'b', 'c', 'd' or 'e' are in the
#string using five diffferent if statements.
#Print appropriate output in each case.
#Use loops, comparison operators, decision structures
#and codes for the different letters of the alphabet.
if 'a' in word:
    print("a is in the word.")
else:
    print("a is not in the word.")
if 'b' in word:
    print("b is in the word.")
else:
    print("b is not in the word.")
if 'c' in word:
    print("c is in the word.")
else:
    print("c is not in the word.")
if 'd' in word:
    print("d is in the word.")
else:
    print("d is not in the word.")
if 'e' in word:
    print("e is in the word.")
else:
    print("e is not in the word.")
    
for u in range(65,91):#There is a loop through uppercase letters.
    if chr(u) in word:#(f) Check if each letter in the alphabet is in the string
        print(chr(u)+"is in the word.")#Print appropriate output.
    else:
        print(chr(u)+"is not in the word.")
for l in range(97,123):#There is a loop through lowercase letters.
    if chr(l) in word:
        print(chr(l)+"is in the word.")
    else:
        print(chr(l)+"is not in the word.")        
    
>>>>>>> c65b72842c94ac3d74cf98e6207d6106d0927b6d
