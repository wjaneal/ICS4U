"""
name:khan
date:20180110
program title:assignment 1
purpose: find all the numbers that are divisible by 3 or 19 in interval [1,1000]
"""

for i in range (1,1001):
# so that it will be 1000 numbers 
    print (i)
    if i % 3 == 0:
        print (str(i)+' is divisible by 3')
    if i % 19 == 0:
        print (str(i)+' is divisible by 19')
