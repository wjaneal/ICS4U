# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 13:41:58 2018

@author: Mike + Jeff
"""

class Basic:
    
    def convert_to_binary(self,originString):
        self.originString = str(input(' '))
        self.binaryString = ' '.join(format(ord(x),'b')for x in self.originString)
        print(self.binaryString)
        return self.binaryString
    
    def binary_to_chaos(self,binaryString):
        self.listB = []
        self.listB = self.binaryString.split(' ')
        return self.listB
        
    def chaos_to_binary(self,chaosString):
        pass
    
    def binary_to_orgin(self,binaryString):
        pass
    

Basic.convert_to_binary()

#Basic.binary_to_chaos()