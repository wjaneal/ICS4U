"""
Name: Jeffrey
Date: Jan 11, 2018
Title: Assignment
Purpuse:
(a) Let the user input two numbers.
(b) Convert the numbers to integers
(c) Print the sum, difference, product and quotient of the numbers.
(d) Repeat (b) and (c) for floating point
(e) Convert the numbers to strings.
(f) Output the four results as strings as follows: The sum of a and b is 5.667, etc. for subtraction, multiplication and division.
"""

#Let users input two variables:
number1 = input("Please input the first number:  ")
number2 = input("Please input the second number:  ")

#Convert the numbers to integers:
IntNumber1 = int(number1)
IntNumber2 = int(number2)

#Calcutate the sum, difference, product and quotient of the numbers.
IntAdding = IntNumber1 + IntNumber2
IntSubstract = IntNumber1 - IntNumber2
IntProduct = IntNumber1 * IntNumber2
IntQuotient = IntNumber1 / IntNumber2

#Using a dictionary to restore data
IntResults = {"sum: ": IntAdding, "difference: ": IntSubstract, "product: ": IntProduct, "quotient: ": IntQuotient}

#Print the sum, difference, product and quotient of the numbers
for i, v in IntResults.items():
    print(i + str(v))

#Print the results in a floating form
FlAdding = float(number1) + float(number2)
FlSubstract = float(number1) - float(number2)
FlProduct = float(number1) * float(number2)
FlQuotient = float(number1) / float(number2)

FlResults = {"sum: ": FlAdding, "difference: ": FlSubstract, "product: ": FlProduct, "quotient: ": FlQuotient}

for i, v in FlResults.items():
    print(i + str(v))
    
#Output the four results as strings:
print("The sum of a and b is: ", str(IntAdding))
print("The difference of a and b is: ", str(IntSubstract))
print("The product of a and b is: ", str(IntProduct))
print("The quotient of a and b is: ", str(IntQuotient))








