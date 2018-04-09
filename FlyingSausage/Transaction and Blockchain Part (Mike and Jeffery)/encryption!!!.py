# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 13:41:58 2018

@author: Mike + Jeff
"""

class Basic:

    def convert_to_binary(self,originString):
        self.binaryString = ''
        for i in range (len(originString)):
            x = str("{0:b}".format(ord(originString[i])))+' '
            self.binaryString = self.binaryString + x
        return self.binaryString
    
    def binary_to_chaos(self):
        self.chaosString = ''
        self.listB = []
        self.listB = self.binaryString.split(' ')
        self.listB.pop()
        
        for j in range (len(self.listB)):
            if len(self.listB[j]) == 5:
                self.listB[j] = '000' + self.listB[j]
            if len(self.listB[j]) == 6:
                self.listB[j] = '00' + self.listB[j]
            if len(self.listB[j]) == 7:
                self.listB[j] = '0' + self.listB[j]

        for i in range (len(self.listB)):
            x = self.listB[i][:4]
            y = self.listB[i][4:]
            self.listB[i] = y + x
            
        for z in range (len(self.listB)):
            self.chaosString += chr(int(self.listB[z],2))

        print(self.chaosString)
        return self.chaosString
        
    def chaos_to_binary(self):
        self.listC = []
        self.decodeString = ''
        self.chaosString = ' '.join(format(ord(x),'b')for x in self.chaosString)
        self.listC = self.chaosString.split(' ')

        for j in range (len(self.listC)):
            if len(self.listC[j]) == 1:
                self.listC[j] = '0000000' + self.listC[j]
            if len(self.listC[j]) == 2:
                self.listC[j] = '000000' + self.listC[j]
            if len(self.listC[j]) == 3:
                self.listC[j] = '00000' + self.listC[j]
            if len(self.listC[j]) == 4:
                self.listC[j] = '0000' + self.listC[j]
            if len(self.listC[j]) == 5:
                self.listC[j] = '000' + self.listC[j]
            if len(self.listC[j]) == 6:
                self.listC[j] = '00' + self.listC[j]
            if len(self.listC[j]) == 7:
                self.listC[j] = '0' + self.listC[j]

        for i in range (len(self.listC)):
            x = self.listC[i][:4]
            y = self.listC[i][4:]
            self.listC[i] = y + x
            self.decodeString += chr(int(self.listC[i],2))

        print(self.decodeString)
        return self.decodeString
    

st = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()+-*/'
a = Basic()
a.convert_to_binary(st)
a.binary_to_chaos()
a.chaos_to_binary()
