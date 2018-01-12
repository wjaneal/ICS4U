"""
name:khan
date:20180112
program title:assignment 3
purpose:
(a) Let the user input two numbers.
(b) Convert the numbers to integers
(c) Use six comparison operators in six different if statements to compare the two numbers.  Print different outputs for true and false in each case.
(d) Let the user input a string
(e) Determine whether the letters 'a', 'b', 'c', 'd' or 'e' are in the string using five diffferent if statements.  Print appropriate output in each case.
(f) Find a way to check if each letter in the alphabet is in the string (upper and lower case) and print appropriate output. Use loops, comparison operators, decision structures and codes for the different letters of the alphabet.
variable names:a,b,string


"""

a= int(eval(input('give me a number')))
b= int(eval(input('give me a number')))
if a == b :
    print (a,'is equal to',b)
else:
    print (a,'is not equal to',b)
if a!=b:
    print (a,'does not equal',b)
else:
    print (a,'does equal to',b)
if a > b :
        print (a,'is bigger than',b) 
else:
    print (a,'is not bigger than',b)
if a <b:
        print (a,'is smaller than',b)
else:
    print (a,'is not smaller than',b)
if a<=b :
    print (a,'is smaller or equal to',b)
else:
    print (a,'is bigger than',b)
if a>=b :
    print (a,'is bigger or equal to',b)
else:
    print (a,'is smaller than',b)
string=input('give me a word')
for i in range (65,123):
    if chr(i) in string:
        print (chr(i) ,'is in',string)


    
        

         
            
       



