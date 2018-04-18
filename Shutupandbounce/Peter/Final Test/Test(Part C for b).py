#Part C: Algorithms - Search activity


import random
import time
import matplotlib as plt

class searching:
    
    def random_search(ptr,n):    # set a function
        maximun = n
        minimun = 0   #set two boundaries
        start = time.clock() # start the timer
        while maximun - minimun != 1:
            temp = random.randint(0, n-1)
            if set[temp] > ptr and temp > maximun:
                maximun = temp
                if set[temp] < ptr and temp < minimun:
                    minimun = temp
                    return (set[maximun])
        
        elapsed = (time.clock() - start)
        return elapsed
    
    def linear_search(x):   # set a function
        start = time.clock()
        for i in range(0, 10000):  # start a loop for 1000000 numbers
            if i != x:
                i += 1 # add to 1
            else:
                break# break the loop
            elapsed = (time.clock() - start)
        return elapsed# reflect the time on console
        
    def binary_search(plist, pobject , start):  # set a function
        start = time.clock()
        first = 0
        last = 10000
        found = False
        while first <= last and not found:
            midpoint = (first + last) // 2
            if plist[midpoint] == pobject:
                found = True
            else:
                if object < plist[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        return found
        
        elapsed = (time.clock() - start)
        return elapsed
    
    def Data(time, time1, time2):    # give a class structure to put all function in it for caculating
        print ("The Random Searching")
        n = [10,100,1000,10000,100000]
        average = 0
        for i in range (0, 5):
            num = random.randint(0,1000000)
            time = searching.random_search(num)
            text = 'Trial' + str(i) + ' ' + (time)
            print(text)
            average = average + time
        print("average " + str(average/5))
        print('\n')
        plt.ylabel('The First Algorithm for time')
        plt.xlabel('Numbers')
        plt.plot(num, time)
        plt.show()
        
        print ("The Linear Searching")
        for i in range (0, 5):
            num = random.randint(0, 1000000)
            time1 = searching.linear_search(num)
            text1 = 'Trial' + str(i) + ' ' + str(time1)
            print(text1)
            average = average + time1
        print(n, time1)
        print("average" + str(average/5))
        print('\n')
        plt.ylabel('The Second Algorithm for time')
        plt.xlabel('Numbers')
        plt.plot(num, time1)
        plt.show()
        
        print ("The Binary Searching")
        for i in range(0, 5):
            num = random.randint(0,1000000)
            time2 = searching.binary_search(num)
            text2 = "Trial" + str(i) + ' ' + str(time2)
            print(text2)
            average = average + time2
        print("average" + str(average/5))
        print('\n')
        plt.ylabel('The Third Algorithm for time')
        plt.xlabel('Numbers')
        plt.plot(num, time2)
        plt.show()