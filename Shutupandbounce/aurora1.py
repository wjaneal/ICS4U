#(a) Name:Aurora Hou
#(b) Date:2018.01.10 
#(c) Program Title:assgenment 1 (ICS4U)
#(d) Purpose:Loop through 1000 numbers.  Print them.
#            if the number is divisible by 3,print"divisible by 3"
#            if the number is divisible by 19,print"multiple of 19!" 
#loop
for i in range(1,1001):
    if i % 3 == 0:
        print("divisible by 3")
    elif i % 19 == 0:
        print("multiple of 19!")
    else:
        print(i)


