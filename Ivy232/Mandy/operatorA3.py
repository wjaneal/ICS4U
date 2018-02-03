
"""
Mandy Jan.12 2018 Operator
Write a program that does the following:
(a) Let the user input two numbers.
(b) Convert the numbers to integers
(c) Use six comparison operators in six different if statements to compare the two numbers.  Print different outputs for true and false in each case.
(d) Let the user input a string
(e) Determine whether the letters 'a', 'b', 'c', 'd' or 'e' are in the string using five diffferent if statements.  Print appropriate output in each case.
(f) Find a way to check if each letter in the alphabet is in the string (upper and lower case) and print appropriate output. Use loops, comparison operators, decision structures and codes for the different letters of the alphabet.

Part1
"""
a = int(input("Please enter a number!"))
b = int(input("Please enter another number!"))

if a != b:   
    if a >= b :
        print("inequality")
        print(a,"is bigger or equal to",b)
    elif a <= b:
        print("inequality")
        print(a,"is smaller or equal to than",b)
    
if a != b:
    if a > b :
        print(a,"is bigger than",b)
    elif a< b:
        print(a,"is smaller than",b)
elif a ==2:
    print (a,"is equal to",b)
    
"""
Part2
""" 

word = str(input("Please enter a word!"))
letter =str(input("Please enter a letter!"))

if letter in word:
    print("The letter",letter,"is in the word!")
else:
    print("The letter",letter,"is not in the word!")


"""
Part3
"""

def checkLetter(letter,word):
    if letter in word:
        return("The letter",letter,"is in the word!")
    else:
        return("The letter",letter,"is not in the word!")


for i in range (65,91):
    letter = chr(i)
    print (checkLetter(letter,word))


for i in range (97,123):
    letter = chr(i)
    print (checkLetter(letter,word))
