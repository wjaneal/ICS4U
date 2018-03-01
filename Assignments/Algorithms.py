#Algorithms
#Algorithm - a set of instructions to complete a task
#Example - Find the sum of the multiples of 3 or 5 below 1000.
#This example was done in class; the solution is an algorithm

#Sorting
Numbers = [4,734,64,833,7,944,8,95,7]
Numbers.sort()
print(Numbers)
'''
A = [56,7]
Temp = A[0]
A[0] = A[1]
A[1] = Temp
'''
A = [787,23423,2342343,43,465,45,45,46,657]
print(A)
#Find lowest number; find next lowest, etc.
for i in range (0,len(A)):
    #Find the lowest remaining number in the array.
    lowest = A[i]
    lowest_index = i
    for j in range(i, len(A)):
	if A[j] < lowest:
		lowest = A[j]
		lowest_index = j
    #Switch it into position i: 
    Temp = A[i]
    A[i] = lowest
    A[lowest_index] = Temp
print(A)


#Switch two numbers at a time









#Search

#Recursive

#Example - Factorial
#n! = n*(n-1)*(n-2)*(n-3).....(3)(2)(1)
#5! = 5*4*3*2*1 = 120

def loop_factorial(n):
    F = 1
    for i in range(1,n+1):
	F*=i
    return F

def recursive_factorial(n):
    if n>1:
        return n*recursive_factorial(n-1)
    else:
        return 1


print("Factorial (500):", loop_factorial(500))
print("Factorial (500):", recursive_factorial(500))














#Benchmarking

