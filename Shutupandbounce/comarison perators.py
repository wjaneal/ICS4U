'''
Assignment 3
2018/01/12
Halley Qiu
Comparison operators
Purpose:
(a) Let the user input two numbers.
(b) Convert the numbers to integers
(c) Use six comparison operators in six different if statements to compare the two numbers.  Print different outputs for true and false in each case.
(d) Let the user input a string
(e) Determine whether the letters 'a', 'b', 'c', 'd' or 'e' are in the string using five diffferent if statements.  Print appropriate output in each case.
(f) Find a way to check if each letter in the alphabet is in the string (upper and lower case) and print appropriate output. Use loops, comparison operators, decision structures and codes for the different letters of the alphabet.
Variable Names: a, b
'''
#let the user input two numbers, and converts to integers.
x = int(input('Could you give a number? '))
y = int(input('Could you give me another one?'))
#use sic comparison operators in six different if statements, and print True and False in each case.
if x > y:
    print('x is greater than y. ')
else:
    print('x is not greater than y. ')
if x < y:
    print('x is less than y.')
else:
    print('x is not less than y.')
if x >= y:
    print('x is greater than or equal to y. ')
else:
    print('x is not greater than or equal to y. ')
if x <= y:
    print('x is less than or equal to y.')
else:
    print('x is not less than or equal y.')
if x == y:
    print('x is equal to y.')
else:
    print('x is not equal to y.')
if x != y:
    print('x is not equal to y. ')
else:
    print('x is equal to y. ')
#Let the user put a string
string = input('Could you please input a string?')
#Checks whether 'a', 'b', 'c', 'd', 'e' are in a string and print different statements
if 'a' in 'string':
    print("a is in the string.")
else:
    print("a is not in the string")
if 'b' in 'string':
    print("b is in the string.")
else:
    print("b is not in the string.")
if 'c' in 'string':
    print("c is in the string.")
else:
    print("c is in the string.")
if 'd' in 'string':
    print("d is in the string.")
else:
    print("d is in the string.")
if 'e' in 'string':
    print("e is in the string.")
else:
    print("e is in the string.")

#automatically checks whether each letter is in the string
for lowerCase in range(97,123): #loops through lowercase letters
    if chr(lowerCase) in string: #checks whether the lowercase letter is in the string
        print(chr(lowerCase)+" is in the string")
    else:
        print(chr(lowerCase)+" is not in the string")
for upperCase in range(65,91):#loops through uppercase letters
    if chr(upperCase) in string: #checks whether the uppercase letter is in the string
        print(chr(upperCase)+" is in the string")
    else:
        print(chr(upperCase)+" is not in the string")


    
    
    
    


    
    
    
