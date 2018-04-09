# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 13:41:58 2018

@author: Mike + Jeff
"""

class Basic: #This creates a class

    def convert_to_binary(self,originString): #This defines convert the origin string to binary string
        self.binaryString = '' #This creates a string
        for i in range (len(originString)): #This loop convert each character in the string into the binary
            x = str("{0:b}".format(ord(originString[i])))+' ' #This convert the character into the binary
            self.binaryString = self.binaryString + x #This connects all the binary string together to a the long binary string
        return self.binaryString #This returns the binary string
    
    def binary_to_chaos(self): #This defines convert the binary string to chaos string
        self.chaosString = '' #This creates a string
        self.listB = [] #This creates a list 
        self.listB = self.binaryString.split(' ') #This split the binary string into a list
        self.listB.pop() #This delete the unnecessary space at the end of the list
        
        for j in range (len(self.listB)): #This loop converts all the binary data into 8 digits to make it easier for encryption
            if len(self.listB[j]) == 5: #This if statement changes the binary with 5 digits to 8 digits
                self.listB[j] = '000' + self.listB[j] #This adds three zeros before each binary string with 5 digits
            if len(self.listB[j]) == 6: #This if statement changes the binary with 6 digits to 8 digits
                self.listB[j] = '00' + self.listB[j] #This adds two zeros before each binary string with 6 digits
            if len(self.listB[j]) == 7: #This if statement changes the binary with 7 digits to 8 digits
                self.listB[j] = '0' + self.listB[j] #This adds one zero before each binary string with 7 digits

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
    

st = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()+-*/' #This creates a string to encrypt and decrypt

#This runs the program
a = Basic()
a.convert_to_binary(st)
a.binary_to_chaos()
a.chaos_to_binary()
