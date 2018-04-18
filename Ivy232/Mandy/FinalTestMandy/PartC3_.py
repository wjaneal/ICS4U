#3a)
def f(n):
    if n == 0:
        return 2
    else:
        return 3*f(n-1) + 2
A = []
for i in range(0,10000000000000):
    if f(i)<40000000:
        A.append(i)
    else:
        break

print("The number of values is:")
print(len(A))

#3b)
def It(x):
    if f(x) < 40000000:
        return "True"
    else:
        return "False"
x = int(input("Please enter a possible integer!"))

print(It(x))
