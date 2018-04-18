#define a function to realize the equation
def f(n):
    #move on
    if n > 0:
        return (3*f(n - 1)+2)
    #stop
    if n == 0:
        return 2
#initiation
n1 = 0
a = 1
#until the f(x) is greater than 40000000, it will not stop
while f(n1) < 40000000:
    n1 = n1 + 1
    a = a + 1
#print the amount of the proper number
print(a-1)

#define a function to check whether the number is valid
def checkIt(x):
    #move on
    if x > 2:
        #help verify
        if (x-2) % 3 == 0:
            return checkIt((x-2)/3)
        else:
            return "false"
    #stop
    if x == 2:
        return "true"
#input the number you want to test
m = int(input("What number do you want to test?"))
#output the result
print(checkIt(m))

