#Program setup - numbers
import random
import pickle
######################
EvenTarget = 2 
EvenTarget = 4
SameLastTarget = 2
HotTarget = 4
SequentialTarget = 2
Lottery = "Lotto_649.dat"
#Lottery = "Lotto_Max.dat"
if Lottery == "Lotto_649.dat":
	Lotto_Size = 6
if Lottery == "Lotto_Max.dat":
	Lotto_Size = 7
######################
Total = 0
placeholder = 0 
Max_Number = 49
Hot = 3
Cold = 0
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
	EvenCount = 0
	while count < Size:
		if isEven(numbers[count]):
			EvenCount += 1
		count+=1
	return EvenCount

def SequentialCount(numbers):
	q1 = 0
	q2 = 0
	SequentialCount = 0
	while q1 < len(numbers)-1:
		q2 = q1
		while q2 < len(numbers):
			if Sequential(numbers[q1], numbers[q2]):
				SequentialCount += 1
			q2 +=1
		q1+=1
	return SequentialCount

def SameLastCount(numbers):
	q1 = 0
	q2 = 0
	Size = len(numbers)
	SameLast_Num = 0
	while q1 < Size-1:	
			q2 = q1
			while q2 < Size:
				if SameLast(numbers[q1], numbers[q2]):
					SameLast_Num +=1
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


Size = 50
f = open(Lottery,'rb')
grid = [0]*(Size*Lotto_Size)
placeholder = pickle.load(f)
grid = pickle.load(f)
print placeholder
f.close()
print grid
Even = 0	
Numbers = [0]*Size
count = 0 
for n in grid:
	#print "Testing...", n, n/2, int(n/2)
	if n/2 == int(n/2) and n <> 0:
		Even +=1
	if n <> 0:
		Total += 1
	Numbers[n]+=1

count = 0
while count < len(Numbers):
	print count, Numbers[count]
	count +=1
Minimum = Min(Numbers)
Maximum = Max(Numbers)
count = Minimum
while count <= Maximum:
	q = 0
	while q < Size:
		if count == Numbers[q]:
			print q, count
		q+=1
	count += 1

count = 0
Trial = [0]*(Lotto_Size)
DoubleCheck = [0]*(Max_Number+1)
while count < 100:
	q = 0
	DoubleCheck = [0]*(Max_Number+1)
	while q < Lotto_Size:
	        accept = 0
		while accept == 0:
			Trial[q] = int(random.random()*Max_Number+1)
			#print "Testing", q, Trial[q], DoubleCheck, DoubleCheck[Trial[q]]
			if DoubleCheck[Trial[q]] == 0:
				accept = 1
				DoubleCheck[Trial[q]] = 1
		q+=1
	S = SequentialCount(Trial)
	H = HotCount(Trial, Numbers, Hot)
	E = CountEven(Trial)
	#print "Testing", Even, len(grid)
	EvenTarget = int(Lotto_Size*Even/Total)+1

	SL = SameLastCount(Trial)
	Score = -(S-SequentialTarget)*(S-SequentialTarget)-(H-HotTarget)*(H-HotTarget)-(SL-SameLastTarget)*(SL-SameLastTarget)-(E-EvenTarget)*(E-EvenTarget)

	if Score > -30:
		print Trial, SequentialCount(Trial), CountEven(Trial), SameLastCount(Trial), HotCount(Trial, Numbers, Hot), Score

	count +=1
	#print EvenTarget
