Fibonacci=[]
term1=1
term2=1
total = 0
while term2 <=4000000:
	temp = term1+term2
	term1=term2
	term2=temp
	if term2%2==0:
		Fibonacci.append(term2)
		print(term2)
		total+=term2
print(Fibonacci)
print("The sum of the even Fibonacci terms is ", total)
