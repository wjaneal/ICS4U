

import random
import math
from time import *
import cProfile
import MySQLdb

conn = MySQLdb.connect (host = "localhost",
                           user = "root",
                           passwd = "**********",
                           db = "lotto")
#f = open('Matrix.dat', 'wb')
#Connect to the Database and fetch the most recent lottery numbers:
Lottery = 0
while Lottery < 1 or Lottery > 2:
        Lottery = input("Please select a lottery: (1) - 649; (2) - Max")
if Lottery == 1:
        LotterySize = 6
	LottoString = "lotto649"
else:
        LotterySize = 7
	LottoString = "lottomax"

#Setup the empty data.
P1 = [0.0]*(LotterySize)
P2 = P1
P3 = P2
Target = P3

cursor = conn.cursor()
cursor.execute("SELECT * from "+LottoString+" order by drawdate DESC LIMIT 4")
rows = cursor.fetchall()
for i in range(0,LotterySize):
	P1[i] = int(str(rows[0][i])[:])
	P2[i] = int(str(rows[1][i])[:])
	P3[i] = int(str(rows[2][i])[:])
	Target[i] = int(str(rows[3][i])[:])

print P1, P2, P3, Target
P1 = [P1]
P2 = [P2]
P3 = [P3]
Target = [Target]

 
def zero(m,n):
    # Create zero matrix
    new_matrix = [[0 for row in range(n)] for col in range(m)]
    return new_matrix
 
def rand(m,n):
    # Create random matrix
    new_matrix = [[random.random() *2-1 for row in range(n)] for col in range(m)]
    return new_matrix
 
def show(matrix):
    # Print out matrix
    for col in matrix:
        print col 
 
def mult(matrix1,matrix2):
    # Matrix multiplication
    if len(matrix1[0]) != len(matrix2):
        # Check matrix dimensions
        print 'Matrices must be m*n and n*p to multiply!'
    else:
        # Multiply if correct dimensions
        new_matrix = zero(len(matrix1),len(matrix2[0]))
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    new_matrix[i][j] += matrix1[i][k]*matrix2[k][j]
        return new_matrix

def add_matrix(matrix1, matrix2):
	if len(matrix1[0]) != len(matrix2[0]) or len(matrix1) != len(matrix2):
		print "Matrices must be the amse dimension to add!"
	else:
		new_matrix= zero(len(matrix1),len(matrix1[0]))
		for i in range(len(matrix1)):
			for j in range(len(matrix1[0])):
				new_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
		return new_matrix

def sub_matrix(matrix1, matrix2):
	if len(matrix1[0]) != len(matrix2[0]) or len(matrix1) != len(matrix2):
		print "Matrices must be the amse dimension to add!"
	else:
		new_matrix= zero(len(matrix1),len(matrix1[0]))
		for i in range(len(matrix1)):
			for j in range(len(matrix1[0])):
				new_matrix[i][j] = matrix1[i][j] - matrix2[i][j]
		return new_matrix

def difference_of_squares(matrix1, matrix2):
	if len(matrix1[0]) != len(matrix2[0]) or len(matrix1) != len(matrix2):
		print "Matrices must be the amse dimension to add!"
	else:
		sum = 0
		for i in range(len(matrix1)):
			for j in range(len(matrix1[0])):
				sum+= (matrix1[i][j] - matrix2[i][j])**2
		return sum


def time_mult(matrix1,matrix2):
    # Clock the time matrix multiplication takes
    start = clock()
    new_matrix = mult(matrix1,matrix2)
    end = clock()
    print 'Multiplication took ',end-start,' seconds'
 
def profile_mult(matrix1,matrix2):
    # A more detailed timing with process information
    # Arguments must be strings for this function
    # eg. profile_mult('a','b')
    cProfile.run('matrix.mult(' + matrix1 + ',' + matrix2 + ')')



def DifferentialPropagate(i, j, P,A, ConvergenceRate, Target):
	#Determines the differential effect on the target values of a change in a matrix element
	#and accordingly applies a perturbation to the element.
	#print i, j, P, A, ConvergenceRate, Target
	DifferentialPropagationElement1 = P[0][j]*(A[i][j]-ConvergenceRate)
	DifferentialPropagationElement2 = P[0][j]*(A[i][j]+ConvergenceRate)
	Difference1 = abs(DifferentialPropagationElement1-Target[0][j])
	Difference2 = abs(DifferentialPropagationElement2-Target[0][j])
	if Difference1*Difference2 < 0:
		if Difference1 < Difference2:
			return +ConvergenceRate
		elif Difference1 > Difference2:
			return ConvergenceRate
	else:
		return 0

	

def Propagate(A,B,C,P3,P2,P1):
	D = mult(P3, A)
	E = mult(P2, B)
	F = mult(P1, C)
	Sum = add_matrix(D,E)
	Sum = add_matrix(Sum, F)
	return Sum

iterations = 100000

A = rand(LotterySize,LotterySize)
B = rand(LotterySize,LotterySize)
C = rand(LotterySize,LotterySize)
bestA = zero(LotterySize, LotterySize)
bestB = zero(LotterySize, LotterySize)
bestC = zero(LotterySize, LotterySize)

#if Lottery == 1:
#	P3 = [[12,16,19,34,41,47]]
#	P2 = [[1, 18, 25,26, 36, 39]]
#	P1 = [[1, 22, 28, 38, 47, 48]]
#	Target = [[2, 11, 21, 28, 31, 34]]
#else:
#	P2 = [[11,24,26,31,42,44,46]]
#	P1 = [[3, 4, 9, 25, 26, 37, 39]] 
#	P3 = [[3, 11, 18, 19, 23, 27, 44]]
#	Target = [[2,13,22,28,35,41,42]]	
ConvergenceRate = 0.1
bestError = 1000

D = mult(P3,A)
E = mult(P2,B)
F = mult(P1,C)
Sum = add_matrix(D,E)
Sum = add_matrix(Sum, F)

for Iteration in range(1, iterations):
	A = rand(LotterySize,LotterySize)
	B = rand(LotterySize,LotterySize)
	C = rand(LotterySize, LotterySize)
	
	Sum = Propagate(A,B,C,P3,P2,P1)

	Error = difference_of_squares(Sum, Target)
	if Error < bestError:
		bestError = Error
		bestA = A
		bestB = B
		bestC = C
	print Iteration, Error
bestA1 = bestA
bestB1 = bestB
bestC1 = bestC
A = bestA
B = bestB
C = bestC


for Iteration in range(1, iterations):
	if Iteration % iterations/10 == 0:
		ConvergenceRate /= 10.0
	dA = zero(LotterySize, LotterySize)
	dB = zero(LotterySize, LotterySize)
	dC = zero(LotterySize, LotterySize)
	for i in range(0, LotterySize-1):
		for j in range(0, LotterySize-1):
			dA[i][j] += DifferentialPropagate(i, j, P3, A, ConvergenceRate, Target)
			dB[i][j] += DifferentialPropagate(i,j,P2,B,ConvergenceRate, Target)
			dC[i][j] += DifferentialPropagate(i,j,P1, C, ConvergenceRate, Target)
	A = add_matrix(A, dA)
	B = add_matrix(B, dB)
	C = add_matrix(C, dC)
	Sum = Propagate(A,B,C,P3,P2,P1)

	Error = difference_of_squares(Sum, Target)
	if Error < bestError:
		bestError = Error
		bestA = A
		bestB = B
		bestC = C
	print Iteration, Error
	

Sum1 = Propagate(bestA1,bestB1, bestC1, P3, P2, P1)
print Sum1, Target, difference_of_squares(Sum1,Target)
Sum2= Propagate(bestA, bestB, bestC, P3,P2,P1)
print Sum2, Target, difference_of_squares(Sum2, Target) 

R1 = mult(P2, A)
R2 = mult(P1, B)
R3 = mult(Target, C)
Result = add_matrix(R1,R2)
Result = add_matrix(Result, R3)
for i in range(0, len(Result[0])):
	Result[0][i] = int(Result[0][i]) % 49 + 1
print Result
valueString = ""
for i in range(0, len(Result[0])-1):
	valueString+=str(Result[0][i])+", "
valueString += str(Result[0][len(Result[0])-1])
if LotterySize == 6:
	valueString+=', 0'

print valueString

cursor.execute("INSERT into chosen (n1, n2, n3, n4, n5, n6, n7) values ("+valueString+")")

'''D = mult(P3,A)
Sum1 = add_matrix(D,E)
Sum1 = add_matrix(Sum1,F)


print Sum
print Sum1
print sub_matrix(Sum, Sum1)
'''
