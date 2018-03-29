# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 13:41:58 2018

@author: Mike + Jeff
"""

class Basic:

    def convert_to_binary(self,originString):
        self.binaryString = ' '.join(format(ord(x),'b')for x in originString)
        #print(self.binaryString)
        return self.binaryString
    
    def binary_to_chaos(self):
        self.chaosString = ''
        self.listB = []
        self.listB = self.binaryString.split(' ')
        #print(self.listB)
        for i in range (len(self.listB)):
            self.listB[i] = self.listB[i][::-1]
            self.chaosString += chr(int(self.listB[i],2))
        print(self.listB)
        print(self.chaosString)
        return self.chaosString
        
    def chaos_to_binary(self):
        self.listC = []
        self.decodeString = ''
        self.chaosString = ' '.join(format(ord(x),'b')for x in self.chaosString)
        self.listC = self.chaosString.split(' ')
        print(self.listC)
        for i in range (len(self.listC)):
            self.listC[i] = self.listC[i][::-1]
            self.decodeString += chr(int(self.listC[i],2))
        print(self.decodeString)
        return self.decodeString
    
    def binary_to_orgin(self):
        
        pass
    

st = 'eiaoieeou'
a = Basic()
a.convert_to_binary(st)
a.binary_to_chaos()
a.chaos_to_binary()
