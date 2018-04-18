# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 00:38:43 2018

@author: 11256
"""

class fruit:
    def __init__(self):
        self.name = ['apples','bananas','pears','strawberry','watermelon']
        self.quantity = ["10","5","4","7","6"]
        self.price = ["5","3","4","6","8"]
        
    def getName(self):
        print (self.name)
    
    def getPrice(self):
        print (self.price)
    
    def getQuantity(self):
        print (self.quantity)
        
class fruitstand:
    def __init__(self, fruitList, fruitPrices, fruitQuantities):
        self.fruitAvailable = []
        self.fruitList = self.name
        self.fruitPrice = self.price
        self.Quantities = self.quantity
        for i in range(0,len(fruitList)):
            self.fruitAvailable.append(fruit(fruitList[i],fruitPrices[i],fruitQuantities[i]))
    
    def purchase(self,tradeName,tradeNumber,tradePrice):
        print ("Hi",self.shopperName)
        print (self.shopperMoney)
        print (self.fruitAvailable)
        while self.shopperCash <= 0:
            self.tradeName = input("What do you want to buy?")
            if tradeName in self.name:
                i  = self.name.index(self.tradeName)
                self.tradeNumber = str(input("How much do you want to buy?"))
                if self.tradeNumber <= self.quantity[i]:
                    self.quantity[i] -= self.tradeNumber
                    self.tradePrice = self.tradeNumber * self.price[i]
                    print ("You have to pay",self.tradePrice)
                    if self.tradePrice <= self.shopperCash:
                        print (self.tradeName + self.quantity[i])
                        self.shopperCash -= tradePrice
                    else:
                        print ("You do not have enough money.")
                        self.quantity[i] = self.shopperCash / self.price[i]
                        print (self.tradeName + self.quantity[i])
                else:
                        print ("We do not have enough iventory.")
                        print (self.tradeName + self.quantity[i])
            else:
                print("We do not have this fruit.")
            print ("See you next time!")
        
class shopper:
    def __init__(self,shopperName,shopperCash):
        self.shopperName = input("What is your name?")
        self.shopperCash = str(input(("How much money do you have?"))
        while self.shopperCash > 0:
            I = []
            I.append(self.tradeName + self.tradeNumber)
            print (I)
        print (self.shopperCash)
F = fruitstand
S = shopper
Fr = fruit
F.purchase
S.__init__
            
            