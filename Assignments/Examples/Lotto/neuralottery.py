#''' Neural Network Lottery Program - Design
#
#1 - Load Data
#Repeat for the required number of epochs / expected error level:
#	2 - Extract indicators for memory level
#	3 - Feed neural network
#	4 - Train neural network
#Make prediction
#
#
#Initialize the weights in the network (often randomly)
#  Do
#         For each example e in the training set
#              O = neural-net-output(network, e) ; forward pass
#              T = teacher output for e
#              Calculate error (T - O) at the output units
#              Compute delta_wh for all weights from hidden layer to output layer ; backward pass
#              Compute delta_wi for all weights from input layer to hidden layer ; backward pass continued
#              Update the weights in the network
#  Until all examples classified correctly or stopping criterion satisfied
#  Return the network
#'''
#
#'''This is the unit element of the neural network'''
#
##############################################################################################################################################
# Setup - Import Libraries
##############################################################################################################################################
import math
import random
import pickle
##############################################################################################################################################
# Setup variables - processing of previous lottery numbers
##############################################################################################################################################
EvenTarget = 2 
EvenTarget = 4
SameLastTarget = 2
HotTarget = 4
SequentialTarget = 2
Total = 0
placeholder = 0 
Max_Number = 49
Hot = 3
Cold = 0
Size = 50
##############################################################################################################################################
#Setup  - Which Lottery to Prognosticate
##############################################################################################################################################
LotteryChoice = 0
while LotteryChoice < 1 or LotteryChoice > 2:
	LotteryChoice = input("Please select: (1) - 649; (2) - Max")
if LotteryChoice == 1:
	Lottery = "Lotto_649.dat"
if LotteryChoice ==2:
	Lottery = "Lotto_Max.dat"

if Lottery == "Lotto_649.dat":
	Lotto_Size = 6
if Lottery == "Lotto_Max.dat":
	Lotto_Size = 7

##############################################################################################################################################
# Determine which numbers have already been chosen by the Matrix Program
##############################################################################################################################################
#Set up a blank list of numbers already chosen
AlreadyChosen = [0]*7
#Set up the connection to the MYSQL database
import MySQLdb
conn = MySQLdb.connect (host = "localhost",
                           user = "root",
                           passwd = "***********",
                           db = "lotto")
cursor = conn.cursor()
#Query the numbers already chosen
cursor.execute("""SELECT * from chosen order by id DESC limit 1 """)
rows = cursor.fetchall()
print rows
for i in range(0, len(rows[0])-1):
	AlreadyChosen[i] = rows[0][i]
	
for i in range(0, len(AlreadyChosen)):
	AlreadyChosen[i] = int(AlreadyChosen[i])
print AlreadyChosen
##############################################################################################################################################
#Setup - Define the Neural Network
##############################################################################################################################################

#Network definition
Input_Layer = 10
Middle_Layer = 10 
Output_Layer = 49

#Test Data
Input_Vector = [0.0]*Input_Layer
Test_Vector = [1.0]*Input_Layer #For testing the network.
#Output_Target = [0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output_Target = [0,1]

#Threshold Value
Threshold = 0.012

#Epochs
Epochs = 3000

#Learning Rate:
Gamma = 0.0001

#Momentum Term
Alpha = 0.0001

#Rounds
rounds = 2
Tally = [0]*(Output_Layer+1)
##############################################################################################################################################
#Class Definitions
##############################################################################################################################################

class Neuron:
	def __init__(self, forward, threshold_value):
		self.input_val = 0.0
		self.weight = [0.0]*(forward)
		self.delta_w = [0.0]*(forward)
		self.previous_delta_w = [0.0]*(forward)
		for i in range(0,forward):
			#For testing:
			#self.weight[i] = i
			#For operation:
    			self.weight[i] = random.random()*2.0-1.0
		self.threshold_val = threshold_value

	def adjust_weights(self, dw):
		self.weight += dw

	
	def threshold(self, input_val):
		#Need to adjust this
		if input_val < self.threshold_val:
			return 0
		else:
			return 1

	def Sum_Junction(self, Inputs, Weights):
		Size_I = len(Inputs)
		Size_W = len(Weights)
		Junction_Sum = 0
		if Size_I == Size_W:
			#print Inputs, Weights
			Junction_Sum = Dot_Product(Inputs, Weights)	
		else:
			print"Error! Returning 0"

		return Junction_Sum		

##############################################################################################################################################
#Function Definitions - Basic Math
##############################################################################################################################################

def sigmoid(input_val):
	return (1/(1+math.exp(-input_val)))

def hyperbolic_tangent(input_val):
	return (1-math.exp(-input_val))/(1+math.exp(-input_val))



def SameLast(a, b):
        if a % 10 == b % 10:
                 return 1
        else:
                return 0

def Sequential(a,b):
        if a-b == 1 or b-a == 1:
                return 1
        else:
                return 0


def isEven(a):
	a = 1.0*a
	if a/2 == int(a/2):
		return 1
	else:
		return 0


def CountEven(numbers):
	Size = len(numbers)
	count = 0
	EvenCount = 0.0
	while count < Size:
		if isEven(numbers[count]):
			EvenCount += 1.0
		count+=1
	return EvenCount

def SequentialCount(numbers):
	q1 = 0
	q2 = 0
	SequentialCount = 0.0
	while q1 < len(numbers)-1:
		q2 = q1
		while q2 < len(numbers):
			if Sequential(numbers[q1], numbers[q2]):
				SequentialCount += 1.0
			q2 +=1
		q1+=1
	return SequentialCount

def SameLastCount(numbers):
	q1 = 0
	q2 = 0
	Size = len(numbers)
	SameLast_Num = 0.0
	while q1 < Size-1:	
			q2 = q1
			while q2 < Size:
				if SameLast(numbers[q1], numbers[q2]):
					SameLast_Num +=1.0
				q2 += 1	
			q1 += 1
	return SameLast_Num

def Min(grid):
	size = len(grid)
	count = 0
	while count < size:
		if count == 0:
			Min = grid[0]
		if grid[count] < Min:
			Min = grid[count]
		count += 1
	return Min

def Max(grid):
	size = len(grid)
	count = 0
	while count < size:
		if count == 0:
			Max = grid[0]
		if grid[count] > Max:
			Max = grid[count]
		count += 1
	return Max

def HotCount(grid, Numbers, Hot):
	Size = len(grid)
	count = 0
	HotCount = 0
	while count < Size:	
		#print count, grid[count], Numbers[grid[count]]
		if Numbers[grid[count]] >= Hot:
			HotCount+=1
		count += 1
	return HotCount

#Extract a set of lottery numbers from the un-pickled data array - index is a counting variable to scan through all of the numbers stored
def Extract_Numbers(Vector, index, Lotto_Size):
	count = 0
	while count < Lotto_Size:
		Return_Vector[count] = Vector[index+count]
		count += 1
	return Return_Vector

def Average(Vector):
	Num_Sum = 0.0
	Size = len(Vector)
	for i in range(0, Size):
		Num_Sum += Vector[i]
	return Num_Sum/Size

def Standard_Deviation(Vector):
	Num_Sum = 0.0
	Sq_Sum = 0.0
	Size = len(Vector)
	Avg = Average(Vector)
	for i in range(0, Size):
		Num_Sum += (Vector[i] - Avg)**2
	return (Num_Sum/Size)**(0.5)

def Magnitude(Vector):
	Size = len(Vector)
	Magnitude = 0.0
	for i in range(0, Size):	
		Magnitude += Vector[i]*Vector[i]
	return Magnitude**(0.5)

def Dot_Product(Vector_U, Vector_V):
#Note: Vectors U and V should be the same size
	Size_U = len(Vector_U)
	Size_V = len(Vector_V)
	Dot_Prod = 0.0
	for i in range(0, Size_U):
		#print "Dot Product: ", Vector_U, Vector_V
		Dot_Prod += Vector_U[i]*Vector_V[i]
	return Dot_Prod

##############################################################################################################################################
#Function Definitions - Neural Network Specific
##############################################################################################################################################

def output_delta(gamma, y, e, alpha, w):
	return (gamma*(y)*(1-y)*(e-y)*y+alpha*w)

def hidden_delta(Hidden_Neuron, y, alpha, w):
	Hidden_Neuron_Size = len(Hidden_Neuron.weight)
	Error_Sum = 0
	for i in range(0, Hidden_Neuron_Size):
		Error_Sum += Hidden_Neuron.weight[i]*Hidden_Neuron.delta_w[i]
	return (y*(1-y)*Error_Sum+alpha*w)

#def error():

def Forward_Propagate(Input_Vector, Input_Neurons, Middle_Neurons, Output_Neurons):
	Input_Size = len(Input_Vector)
	Size_Check = len(Input_Neurons)
	Middle_Size  = len(Middle_Neurons)
	Output_Size = len(Output_Neurons)
	Input_Layer = [0.0]*Input_Size
	Middle_Layer = [0.0]*Middle_Size
	Output_Layer = [0.0]*Output_Size
	#print Input_Size, Middle_Size, Output_Size
	#print "Neurons....: ", Input_Neurons[0].weight, Input_Neurons[0].input_val
	if Input_Size == Size_Check:
		for i in range(0, Input_Size):
			Input_Neurons[i].input_val = Input_Vector[i]
			for j in range(0, Middle_Size):
				Middle_Neurons[j].input_val += Input_Neurons[i].input_val*Input_Neurons[i].weight[j] 
				#print Middle_Neurons[j].input_val, Input_Neurons[i].input_val, Input_Neurons[i].weight[j], "I_M"
		for i in range(0, Middle_Size):
			Middle_Neurons[i].input_val = hyperbolic_tangent(Middle_Neurons[i].input_val)	
		for i in range(0, Middle_Size):
			for j in range(0, Output_Size):
				Output_Neurons[j].input_val += Middle_Neurons[i].input_val*Middle_Neurons[i].weight[j]
				#print Middle_Neurons[i].input_val, Middle_Neurons[i].weight[j], "Test this"	
		for i in range(0, Output_Size):
			Output_Neurons[i].input_val = hyperbolic_tangent(Output_Neurons[i].input_val)		
#		for i in range(0, Middle_Size):
#			for j in range(0, Output_Size):
#				Output_Neurons[j].input_val = hyperbolic_tangent(Dot_Product(Middle_Layer, Output_Neurons[i].weight))

	else:
		print "Error - Something is wrong - check the configuration"	
	#print Middle_Layer, Output_Neurons[i].weight, Output_Layer
#	for j in range(0, Output_Size):
#		print Output_Neurons[j].input_val
	return Output_Neurons

def Back_Propagate(Input_Neurons, Middle_Neurons, Output_Neurons, Output_Vector, Gamma, Alpha):
	Input_Size = len(Input_Neurons)
	Middle_Size = len(Middle_Neurons)
	Output_Size = len(Output_Vector)
	Error_Vector = [0.0]*Output_Size
	for i in range(0, Output_Size):
		Error_Vector[i] = (Output_Vector[i] - Output_Neurons[i].input_val)
	ErrorVal =  "Error: ", Magnitude(Error_Vector)
	#print ErrorVal
	#for i in range(0, Output_Size):
	#	print Output_Neurons[i].input_val
	for i in range(0, Middle_Size):
		for j in range(0, Output_Size):
			Middle_Neurons[i].delta_w[j] = output_delta(Gamma, Middle_Neurons[i].input_val, Error_Vector[j], Alpha,Output_Neurons[j].input_val)
		#print Middle_Neurons[i].delta_w
	for i in range(0, Input_Size):
		for j in range (0, Middle_Size):
			Input_Neurons[i].delta_w[j] = hidden_delta(Middle_Neurons[j], Input_Neurons[i].input_val, Alpha, Middle_Neurons[j].input_val)
	for i in range(0, Middle_Size):
		for j in range(0, Output_Size):
			Middle_Neurons[i].weight[j] -= Middle_Neurons[i].delta_w[j]
	for i in range(0, Input_Size):
		for j in range(0, Middle_Size):
			Input_Neurons[i].weight[j] -= Input_Neurons[i].delta_w[j]
	return ErrorVal
			
#Number of Evens (evens / total)
#Last Digit Counts
#Hot Numbers
#Cool Numbers
#Average
#Standard Deviation
#Vector Magnitude
#Vector Determinant
#Hot Numbers
#Sequential Score



##############################################################################################################################################
#Main Program - Preprocessing for neural network input
##############################################################################################################################################

#Import the grid of numbers according to the selected lottery:
f = open(Lottery,'rb')
grid = [0]*(Size*Lotto_Size)
placeholder = pickle.load(f)
grid = pickle.load(f)
#print placeholder
f.close()
#print grid
Even = 0	
Numbers = [0]*Size
count = 0 

#Lottery Inputs:
#Number of Evens (evens / total)
#Last Digit Counts
#Hot Numbers
#Cool Numbers
#Average
#Standard Deviation
#Vector Magnitude
#Vector Determinant
#Hot Numbers
#Sequential Score

##############################################################################################################################################
#Main Program - Training
#############################################################################################################################################
for round in range(1,rounds):
	Input_Neurons = {}
	Middle_Neurons = {}
	Output_Neurons = {}
	Input_Vector_Size = len(Input_Vector)
	for x in range (0,Input_Layer):
		Input_Neurons[x] = Neuron(Middle_Layer, Threshold)
		Input_Neurons[x].Input_Val = hyperbolic_tangent(Input_Vector[x])
		print "Testing: ", Input_Neurons[x].weight
	for x in range (0,Middle_Layer):
		Middle_Neurons[x] = Neuron(Output_Layer, Threshold)
	for x in range (0,Output_Layer):
		Output_Neurons[x] = Neuron(1, Threshold)


	#Measure the size of the dataset:
	GridCount = 0
	sub_grid = [0.0]*Lotto_Size
	for i in range(0, len(grid)):

		if grid[i] <> 0:
			GridCount += 1
	Epoch_Mod_Val = GridCount / Lotto_Size
	outcome = [0.0]*Lotto_Size
	
	for epoch in range(0, Epochs):
		grid_tab = epoch % Epoch_Mod_Val
		for i in range (0, Lotto_Size):
			sub_grid[i] = grid[grid_tab+i]
			outcome[i] = grid[grid_tab+Lotto_Size+i]
		result = Size*[0]
		for i in range(0,len(outcome)):
			result[outcome[i]] = 1.0
		Input_Vector[0] = CountEven(sub_grid)*1.0
		Input_Vector[1] = SameLastCount(sub_grid)*1.0
		Input_Vector[2] = SequentialCount(sub_grid)*1.0
		Input_Vector[3] = Average(sub_grid)*1.0
		Input_Vector[4] = Magnitude(sub_grid)*1.0
		Input_Vector[5] = Dot_Product(sub_grid, grid)*1.0
		#print CountEven(grid)
		#print grid
		#print Input_Vector, "Input Vector...."
		#The input vector was too wild - tame down its magnitude a little:
		Mag = Magnitude(Input_Vector)
		for x in range(0, len(Input_Vector)):
			Input_Vector[x] = Input_Vector[x] / Mag
	
	
		#Forward Propagate the Network
		#for i in range(0, len(Input_Neurons)):
		#	print Input_Neurons[i].weight
	
		#for i in range(0, len(Middle_Neurons)):
		#	print Middle_Neurons[i].weight
	
		#for i in range(0, len(Output_Neurons)):
		#	print Output_Neurons[i].weight
		Result = Forward_Propagate(Test_Vector, Input_Neurons, Middle_Neurons, Output_Neurons)
		#for i in range(0, Output_Layer):
		#	print Result[i].input_val
			
		print "Testing...."
		#Result = Forward_Propagate(Input_Vector, Input_Neurons, Middle_Neurons, Output_Neurons)
		#for i in range (0, Output_Layer):
			#	print sigmoid(Result[i].input_val)
			#print Output_Target
		Error = Back_Propagate(Input_Neurons, Middle_Neurons, Output_Neurons, Output_Target, Gamma, Alpha)
		
		#Calculate the Square Differences and BackPropagate:
		#BackPropagate(Result, Output_Target)
		if epoch % 1 == 0:
			print epoch, Error
		
	for i in range(0, Output_Layer):
		print Output_Neurons[i].input_val
	Lotto_Picks = [0.0]*Size
	for i in range(0, Size-1):
		Lotto_Picks[i] = i+1
	for i in range(0, Output_Layer):
		print Output_Neurons[i].input_val
	for i in range(0, Output_Layer-1):
		for j in range(i+1, Output_Layer):
			if Output_Neurons[i].input_val < Output_Neurons[j].input_val:
				Temp_Val = Output_Neurons[i].input_val
				Output_Neurons[i].input_val = Output_Neurons[j].input_val
				Output_Neurons[j].input_val = Temp_Val
				Temp_Num = Lotto_Picks[i]
				Lotto_Picks[i] = Lotto_Picks[j]
				Lotto_Picks[j] = Temp_Num
	ResultsArray = [0.0]*Output_Layer*2
	NumbersIndex = 0
	for i in range (0, len(AlreadyChosen)):
		ResultsArray[i] = AlreadyChosen[i]
		NumbersIndex += 1
	NumbersIndexB = 0
	for i in range(0, Output_Layer):
		if Lotto_Picks[i] not in AlreadyChosen and Lotto_Picks[i] <> 0:
			ResultsArray[NumbersIndex+i] = Lotto_Picks[i]
	ResultsArrayDisp = []
	for i in range (0, len(ResultsArray)):
		if ResultsArray[i] <> 0:
			ResultsArrayDisp += [ResultsArray[i]]

		
	print ResultsArrayDisp

#	for i in range(0,Output_Layer):
#		Tally[Lotto_Picks[i]] += 50-i
#Lotto_Picks = [0.0]*Size
#for i in range(0, Size-1):
#	Lotto_Picks[i] = i+1
#
#for i in range(0, Size-2):
#	for j in range(i+1, Size-1):
#		if Tally[i] < Tally[j]:
#			Temp_Num = Tally[i]
#			Tally[i] = Tally[j]
#			Tally[j] = Temp_Num
#			Temp_Num = Lotto_Picks[i]
#			Lotto_Picks[i] = Lotto_Picks[j]
#			Lotto_Picks[j] = Temp_Num

#print Tally
#print Lotto_Picks
	#for x in range (0, Input_Layer):
	#	print Input_Neurons[x].weight
	#for x in range (0, 10):
	#	print Input_Neurons[x].sigmoid(Input_Neurons[x].weight)

	
##############################################################################################################################################
#Main Program - Output
##############################################################################################################################################



#n1 = Neuron()
#print n1.sigmoid(.10002)

