#Name:Peter
#Date:Jan.12.2018
#Title of program:Typecasting
#Purpose:(a) Let the user input two numbers.
#(b) Convert the numbers to integers
#(c) Use six comparison operators in six different if statements to compare the two numbers.
#Print different outputs for true and false in each case.
#(d) Let the user input a string
#(e) Determine whether the letters 'a', 'b', 'c', 'd' or 'e' are in the string using five diffferent if statements.
#Print appropriate output in each case.
#(f) Find a way to check if each letter in the alphabet is in the string (upper and lower case) and print appropriate output. 
#Use loops, comparison operators, decision structures and codes for the different letters of the alphabet.

print ("---------------")
q = int(input("Give you my first number:"))
w = int(input("Give you my first number:"))

if q < w:
    print ('True')
else:
    print ('False')
if q > w:
    print('True')
else:
    print('False')
if q >= w:
    print('True')
else:
    print('False')
if q <= w:
    print('True')
else:
    print('False')
if q == w:
    print('True')
else:
    print('False')
if q!=w:
    print("True")
else:
    print("False")


def f(x):
    return 6*x**2 + 2*x + 10 
print(f(3))

melody = input("Enter a word:")

def checkletter(melody):
    beautiful =("e","r","t","y","u")
    for i in range(1,len(melody)):
        if beautiful in melody:
            return("The letter",beautiful,"is in this blank" )
        else:
            return('nothing')

print (checkletter(melody))
