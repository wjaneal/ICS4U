multiples = []
total = 0
for i in range(1,10):
	if i%3==0 or i%5==0:
		print i
		total+=i
		multiples.append(i)
print (multiples)
print ("The sum of the multiples is:", total)

