#Program setup - numbers
import random
import pickle
placeholder = 0 

Size = 1000

LotteryChoice = 0
while LotteryChoice < 1 or LotteryChoice >2:
	LotteryChoice = input("Choose: (1) - 649; (2) - Max")
if LotteryChoice == 1:
	Lottery = "Lotto_649.dat"
if LotteryChoice == 2:
	Lottery = "Lotto_Max.dat"

if Lottery == "Lotto_649.dat":
        Lotto_Size = 6
if Lottery == "Lotto_Max.dat":
        Lotto_Size = 7

f = open(Lottery,'rb')
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
f = open(Lottery, 'wb')	
pickle.dump(placeholder, f)
pickle.dump(grid, f )
#print placeholder
f.close()
	
