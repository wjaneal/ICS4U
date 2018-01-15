#Name:Peter
#Date:Jan 10 2018
#Title of program: Assignmen (Peter)
#Function of program:Loop through 1000 number
                    #If the number is divisible by 3,print "divisible by 3"
                    #If the number is divisible by 19,print "multiple of 19!"


#Variable names: p

#Loop
for p in range(0,1000):
    if p % 3 == 0:
        print (p,"is divisible by 3")
    elif p % 19 == 0:
        print (p,"is the multiple of 19!")
    else: print (p)