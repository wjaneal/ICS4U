"""
name:khan
date:20180111
program title:assignment 2
purpose: 
    a let the user input two numbers
    b convert the numbers to integers
    c print the sum, difference, product and quotient of the numbers.
    d repeat b adn c for floating point 
    e convert the numbers to strings
    f output the four results as strings as follows: the sum of a and b is 5.667
variable names: a,b,int1,int2,f1,f2
"""

a = eval(input ('give me a number'))
b = eval(input ('give me another number'))
int1= int(a)
int2= int(b)
print('~~~~~~~~~~~~~~ integers')
print('the sum',int1+int2)
print('the difference',int1-int2)
print('product',int1*int2)
print('quotient',int1/int2)
f1= float(a)
f2=float(b)
print('~~~~~~~~~~~~~~ float numbers')
print('the sum',f1+f2)
print('the difference',f1-f2)
print('product',f1*f2)
print('quotient',f1/f2)
print('~~~~~~~~~~~~~~')
print ('the sum of '+str(a) +' and '+ str(b) +' is '+str(f1+f2)) 
print ('the difference of '+str(a) +' and '+ str(b) +' is '+str(f1-f2)) 
print ('the product of '+str(a) +' and '+ str(b) +' is '+str(f1*f2)) 
print ('the quotient of '+str(a) +' and '+ str(b) +' is '+str(f1/f2)) 



