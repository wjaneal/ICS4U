# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 13:32:00 2018
Name: Jaune
Date: Apr. 16, 2018
Purpose:
Title:
@author: CTL
"""
class fruit:
    
    def __init__ (self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def getName(self):
        print(self.name)
    
    def getPrice(self):
        print(self.price)
        
    def getQuantity(self):
        print (self.quantity)
        
class fruitstand:
    
    def __init__(self, fruitName, fruitPrice, fruitQuantity):
        self.fruitList = []
        
        for i in range(0,len(fruitName)):
            self.fruitList.append(fruit(fruitName[i], fruitPrice[i], fruitQuantity[i]))
            
    def purchase(self):
        self.shopperName = input("What is your name:")
        self.shopperCash = input("How much cash do you have right now:")
        self.shopperWant = input("What would you like to buy:")
        self.shopperNumber = input("How many wouold you like to buy:")
        self.fruitAvailable = []
        for i in range(0,len(self.fruitQuantity)):
            self.fruitAvailable.append(fruit(fruitQuantity[i]))


class shopper:
    
    def command(self):
        print("◾Please enter a command:(up to 2 words)")
        self.commandWords = input()
        self.commandList = self.commandWords.split(" ") 
        if len(self.commandList) == 0 or len(self.commandList) > 2:
            print("Please enter a valid command") 
            
        if self.commandList[0] in ["buy", "get", "acquire", "want"]:
            self.shopperCash = input("how much do you have")
            if self.commandList[1] in ["apple"]





fN=["Apple", "Banana", "Orange", "Peach", "Pear"]
fP=[1.50, 2.00, 3.00, 4.20, 5.00]
fQ=[6, 7, 8, 9, 10]

F=fruitstand(fN, fP, fQ)

for i in range(0,len(F.fruitList)):
    print(F.fruitList[i].name+" "+str(F.fruitList[i].price)+" "+str(F.fruitList[i].quantity))

            
            
            
            
            
            
            
        
        
    