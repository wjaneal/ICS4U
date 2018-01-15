'''
Name: Halley Qiu
Date: 2018/1/11
Title: Typecasting
Purpose: Typecast two numbers input by user to different data types and do some calculations
'''
# Let thenuser input two numbers, and convert to integers
x = int(input("Please input a number: "))
y = int(input("Please input another one: "))
intsum = x + y
intdifference = x - y
intproduct = x * y
intquotient = x / y
# print all calculations(results)
print(intsum)
print(intdifference)
print(intproduct)
print(intquotient)
#convert to floating numbers
xfloat = float(x)
yfloat = float(y)
#make floating calculations
floatsum = xfloat + yfloat
floatdifference = xfloat - yfloat
floatproduct = xfloat * yfloat
floatquotience = xfloat / yfloat
# print all floating results
print(floatsum)
print(floatdifference)
print(floatproduct)
print(floatquotience)
# convert results to strings
stringsum = str(floatsum)
stringdifference = str(floatdifference)
stringproduct = str(floatproduct)
stringquotience = str(floatquotience)
# print strings
print('The sum of x and y is', stringsum)
print('The difference of x and y is', stringdifference)
print('The product of x and y is', stringproduct)
print('The quotience of x and y ist', stringquotience)
