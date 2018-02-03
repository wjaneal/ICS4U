#Program setup - numbers
import random
import pickle
placeholder = 0 

def SameLast(a, b):
	if a % 10 == b % 10:
		 return 1
	else:
		return 0

def Sequential(a,b):
	if a-b == 1 or b=a == 1:
		return 1
	else:
		return 0


	
	

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


Size = 50
f = open('Lotto_Data.dat','rb')
Lotto_Size = 6
grid = [0]*(Size*Lotto_Size)
placeholder = pickle.load(f)
grid = pickle.load(f)
print placeholder
f.close()
print grid
	
Numbers = [0]*Size
count = 0 
for n in grid:
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

	
