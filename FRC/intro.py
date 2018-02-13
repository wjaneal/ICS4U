#This file is to introduce the basics of Python.

from math import *
from random import *
#a and b are integer variables
a = 5
b = 6
#numeric variables like integers can be used in 
#arithmetic expressions
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(sin(a/b)+cos(b*a))
print(sqrt(b))
print(b**a)

#friends is a text variable in the form of a list
friends = ["Joe", "Ted", "Sue", "Wendy", "Gina", "Fred"]
friends.append("George")
print(friends)
print(friends[0])
print(friends[1])
#We can use a loop to repeat similar operations.
for i in range(0, 7):
    print(i, friends[i])
for i in range(0,100):
	n1 = int(6*random()+1)
	n2 = int(6*random()+1)
	n3 = n1+n2
	if n3 == 12:
		print("Winner!")
	else:
		print("Try again!")
	print(n1,n2,n3)
n = 0
print(n)
while n < 1000000:
	n = 3*(n+1)
	print(n)

	
 







