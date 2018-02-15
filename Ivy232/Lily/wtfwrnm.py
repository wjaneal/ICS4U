import time
import random
#import decimal

x = []
def bubble_sort(list1):
        for i in range (0, len(list1)-1):
            for j in range(0, len(list1)-1-i):
                if list1[j] > list1[j+1]:
                    list1[j], list1[j+1] = list1[j+1],list1[j]
                    j = j+1
        return list1
        

list2 = random.sample(range(5000), k = 1000)

st = time.time()
bubble_sort(list2)
et = time.time()
print (bubble_sort(list2))
print (et-st)


