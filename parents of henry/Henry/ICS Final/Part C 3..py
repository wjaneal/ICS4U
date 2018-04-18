# -*- coding: utf-8 -*-
class recursion: #This create a class for three recursive algorithms

    def __init__(self):
        self.count = 0

    def function(self,n):
        if n == 0:
            return 2
        else:
            return 3*self.function(n-1) + 2


    def display(self):
        list = []
        for n in range (0,100000):
            if self.function(n) < 40000000:
                list.append(n)
            else:
                pass
        print(list)





    def chekcIt(self,x):
        self.x = int(x)



kashun = recursion()
kashun.display()

