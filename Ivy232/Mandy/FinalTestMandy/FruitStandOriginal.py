#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 13:15:26 2018

@author: xuwentong
"""
        
class fruit: # define fruit: all the fruits have fruit name, quantity and price.

    def __init__(self, fruitName, quantity, price):
        self.fruitName = fruitName
        self.quantity = quantity
        self.price = price
        
    def getName(self): # get name of the fruit(variable).
        print ('%s: %s, %s' % (self.name,self.quantity,self.price))
    def getQuantity(self): # get the quantity of the fruit(variable).
        print ('%s: %s' % (self.name,self.quantity))
    def getPrice(self): # get the Price of the fruit(variable).
        print ('%s: %s' % (self.name,self.price))

class fruitstand(): # define a fruitstand：a list to hold the fruits.

    def __init__(self, list):
        self.F=[]
        self.F.append(fruit("apple",10,1))
        self.F.append(fruit("banana",50,2))
        self.F.append(fruit("grape",10,5))
        self.F.append(fruit("avocado",510,2))
        self.F.append(fruit("strawberry",60,5))

    def purchase(self,fruitName, shopperName, quantity): # buy function
    
        if shopperName.cash >= (fruitName.price*int(quantity)): # judge whether shopper has enough money.
            if quantity <= fruitName.quantity: # judge whether fruitstand stores enough fruit.
                return(fruitName.name,str(quantity))
                
            else:
                quantity = fruitName.quantity # if not, tell the shopper how many (max) this fruit he/she can buy.
                return (fruitName.name,str(quantity))
        else:
            quantity = str(shopper.cash / fruit.price)
            return (fruitName.name, str(quantity))
       
        def get():
            return quantity
class shopper(): # define shoppers with name and cash
    def __init__(self,shopperName,cash,I):
        self.name = shopperName
        self.cash = cash
        # Check....self.FS = fruitstand()
        F = input("") 
        self.FS = fruitstand(F) # import data of fruitstand/ Shoppers stand by the fruitstand.
        #self.FS.F[2].name
        self.I=[] # "Shopper cart"
        '''
        I.append(fruit("apple", 0,1))
        I.append(fruit("banana",0,2))
        I.append(fruit("grape",0,5))
        I.append(fruit("avocado",0,2))
        I.append(fruit("strawberry",0,5))
        '''
    def update(self,fruitName):
        #use a loop to iterate through I until you find the index of Fruitname；
        #update the I using that index value：
        #self.I[index].quantity -= ...
        #self.cash += ...
        #self.FS.F[3].getPrice()
        '''
        for index in (0,len(I)):
            if self.I[index].fruitName == fruitName:
                self.FS.F[index].quantity -= fruitstand.get().quantity
                self.I[index].quantity += quantity
                self.cash = self.cash - fruitName.price * quantity
        '''
        for index in (0,len(self.I)): # Update the infor. for what you buy
            if self.I[index].fruitName == self.F.fruitName: # find out the fruit in the fruitstand
                self.FS.F[index].quantity -= fruitstand.get().quantity # take out from the fruitstand
                self.I[index].quantity += quantity # put into your cart
                self.cash = self.cash - fruitName.price * quantity # pay the money
    def display(): # Demonstrate the infor. for what you buy
        print(self.shoppeName, self.cash, I,F)
        
###########information: database###############
#there is a shopper S whose name is Simon. He has $100. He wants to buy the fruit.        
S = shopper("simon",100,[])
#S.update("apple")
apple = fruit("apple", 45, 1)
banana = fruit("banana",50,2)
grape = fruit("grape",10,5)
avocado = fruit("avocado",510,2)
strawberry = fruit("strawberry",60,5)
F=[]
shopper.F.append(fruit("apple",10,1))
shopper.F.append(fruit("banana",50,2))
shopper.F.append(fruit("grape",10,5))
shopper.F.append(fruit("avocado",510,2))
shopper.F.append(fruit("strawberry",60,5))
