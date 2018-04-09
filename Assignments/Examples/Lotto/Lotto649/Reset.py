#Program setup - numbers
import random
import pickle

Size = 50
f = open('Lotto_Data.dat','wb')
Lotto_Size = 6
grid = [0]*(Size*Lotto_Size)

count = 0
#Option:  Seed the number table with random numbers
#while count < Size:
#	q = 0
#	while q < 6:
#		num = int(random.random()*49+1)
#		grid[num] += 1
#		q += 1
#	count += 1
print grid
placeholder = 0
pickle.dump(placeholder, f)
pickle.dump(grid, f)

