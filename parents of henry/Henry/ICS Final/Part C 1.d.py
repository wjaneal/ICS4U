
import random
import time


class sorting():#This is to create the class
    def bubbleSort(self):  # This is to define a function for bubble sorting Algorithm
        List = []
        for i in range(0,self-2):
            List.append(i)
        List.append(self)
        List.append(self-1)
        startTime = time.clock() #Start to record the time
        for Num in range(len(List) - 1, 0, -1):
            for i in range(Num):
                if List[i] > List[i + 1]:
                    k = List[i]
                    List[i] = List[i + 1]
                    List[i + 1] = k
                else:
                    stop = (time.clock() - startTime)  # This is to end the timer
        return stop

    def insertionSort(self):#This is to define a function for insertion sorting Algorithm
        List = []
        for i in range(0, self - 2):
            List.append(i)
        List.append(self)
        List.append(self - 1)
        startTime =time.clock()
        for index in range(1,len(List)):
            A = List[index]
            B = index

            while B > 0 and List[B-1]>A:
                List[B]=List[B-1]
                B = B-1
            List[B]=A
        stop = (time.clock() - startTime)#This is to end the timer
        return stop

    def selectionSort(self): #This is to define a function for selection sorting Algorithm
        List = []
        for i in range(0, self - 2):
            List.append(i)
        List.append(self)
        List.append(self - 1)
        startTime = time.clock()  # This is to record the start time
        for j in range(len(List) - 1, 0, -1):  # This is to start the loop to make a select sort
            maximumValue = 0
            for k in range(1, j + 1):
                if List[k] > List[maximumValue]:
                    maximumValue = k
            Temp = List[j]
            List[j] = List[maximumValue]
            List[maximumValue] = Temp
        stop = (time.clock() - startTime)#This is to end the time record
        return stop

    def Start():
        sorting.t1 = []
        sorting.t2 = []
        sorting.t3 = []
        #For Bubble sort Alogorithm
        print ('Bubble sort Algorithm: ')
        print ('n     ' + 'Time')
        for N in range (1000,5001,1000):
            Time1 = sorting.bubbleSort(N)
            sorting.t1.append(Time1)
            Output = str(N) + ' ' + str(Time1)
            print(Output)
        print(' ')


        #For Insertion sort Algorithm
        print ('Insertion sort Algorithm: ')
        print ('n     ' + 'Time')
        for N in range (1000,5001,1000):
            Time2 = sorting.insertionSort(N)
            sorting.t2.append(Time2)
            Output = str(N) + ' ' + str(Time2)
            print(Output)
        print(' ')

        # For Selection sort Algorithm
        print('Selection sort Algorithm: ')
        print('n     ' + 'Time')
        for N in range(1000, 5001, 1000):
            Time3 = sorting.selectionSort(N)
            sorting.t3.append(Time3)
            Output = str(N) + ' ' + str(Time3)
            print(Output)
        print(' ')