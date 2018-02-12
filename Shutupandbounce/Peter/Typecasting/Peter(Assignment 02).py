#Name:Peter
#Date:Jan.11.2018
#Title of program:Typecasting
#Purpose:(a) Let the user input two numbers.
#(b) Convert the numbers to integers
#(c) Print the sum, difference, product and quotient of the numbers.
#(d) Repeat (b) and (c) for floating point
#(e) Convert the numbers to strings.
#(f) Output the four results as strings as follows: The sum of a and b is 
#                 5.667,etc.for subtraction, multiplication and division.

#mixedCase variable names:Peter1,Peter2,Parker1,Parker2,m,n

print ('Welcome to Programming World')

#use input statement
m = (input('please enter your first number:'))
print ('Hello!'+ m + ',keep typing')

n = (input('please enter your second number:'))
print ('Thank you,' + n + ',for typing numbers for my programme!')

Peter1 = int(m)
Peter2 = int(n)

print ('Here it is!You get the Integer!')

print ('The sum is',Peter1+Peter2)
print ('The difference is',Peter1-Peter2)
print ('The product is',Peter1*Peter2)
print ('The quotient is',Peter1/Peter2)

Parker1 = float(m)
Parker2 = float(n)

print ('Oh!You get the float!')

print ('The sum is',Parker1+Parker2)
print ('The difference is',Parker1-Parker2)
print ('The product is',Parker1*Parker2)
print ('The quotient is',Parker1/Parker2)

print('And your strings are coming out!')

print ('The sum of ' + str(m) + ' and ' + str(n) + ' is  ' +str(Parker1+Parker2))
print ('The difference of ' + str(m) + ' and ' + str(n) + ' is ' +str(Parker1-Parker2))
print ('The product of ' + str(m) + ' and ' + str(n) + ' is ' +str(Parker1*Parker2))
print ('The quotient of ' + str(m) + ' and ' + str(n) + ' is ' +str(Parker1/Parker2))