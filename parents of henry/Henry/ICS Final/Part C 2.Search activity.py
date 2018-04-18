# -*- coding: utf-8 -*-
import random
import time
class Search():  # This defines a class for three searching method

    def binarySearch(self):
        low = 0
        height = 10
        startTime = time.clock()
        while low < height:
            mid = int((low + height) / 2)
            if mid < self:
                low = mid

            elif mid > self:
                height = mid

            else:
                stop = (time.clock() - startTime)

                return stop

    def start():
        print('Binary search algorithm:')
        print('item :    ' + 'Time ')

        Num = 0.7
        Time3 = Search.binarySearch(Num)
        Output = str(i) + ' ' + str(Time3)
        print(Output)
        Average3 = Average3 + Time3
        print('Average3: ' + str(Average3 / 5))
        print(' ')

Search.start()




