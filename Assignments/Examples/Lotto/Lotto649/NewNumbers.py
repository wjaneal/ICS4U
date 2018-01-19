#Program setup - numbers
import random
import pickle
placeholder = 0 

Size = 50
f = open('Lotto_Data.dat','rb')
Lotto_Size = 6
grid = [0]*(Size*Lotto_Size)
placeholder = pickle.load(f)
grid = pickle.load(f)
print placeholder
f.close()
print grid
Todays_Numbers = [0]*Lotto_Size
count = 0 
while count < Lotto_Size:
	Todays_Numbers[count] = input("Please enter a number")
	count +=1
count = 0
while count < Lotto_Size:
	print int(placeholder)*Lotto_Size+int(count)
	grid[placeholder*Lotto_Size+count] = Todays_Numbers[count]
	count +=1
placeholder += 1
if placeholder > Size:
	placeholder = 0
f = open("Lotto_Data.dat", 'wb')	
pickle.dump(placeholder, f)
pickle.dump(grid, f )
f.close()
	
