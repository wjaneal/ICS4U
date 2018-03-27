# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 13:41:58 2018

@author: Mike + Jeff
"""

import math
class Basic:
    
    def convert_to_binary(self,originString):
        self.binaryString = ' '.join(format(ord(x),'b')for x in self.originString)
        return self.binaryString
    
    def binary_to_chaos(self,binaryString):
        self.divide = math.floor(len(binaryString)/5)
        self.part1 = binaryString[:self.divide]
        self.part2 = binaryString[self.divide:2*self.divide]
        self.part3 = binaryString[2*self.divide:3*self.divide]
        self.part4 = binaryString[3*self.divide:4*self.divide]
        self.part5 = binaryString[4*self.divide:]
        
    
    def chaos_to_binary(self,chaosString):
        pass
    
    def binary_to_orgin(self,binaryString):
        pass
    
