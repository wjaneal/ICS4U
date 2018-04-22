#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 13:15:26 2018

@author: xuwentong
"""
        
class fruit:

    def __init__(self, fruitName, quantity, price):
        self.fruitName = fruitName
        self.quantity = quantity
        self.price = price
        
    def getName(self):
        print ('%s: %s, %s' % (self.name,self.quantity,self.price))
    def getQuantity(self):
        print ('%s: %s' % (self.name,self.quantity))
    def getPrice(self):
        print ('%s: %s' % (self.name,self.price))

class fruitstand():

    def __init__(self, list):
        self.F=[]
        self.F.append(fruit("apple",10,1))
        self.F.append(fruit("banana",50,2))
        self.F.append(fruit("grape",10,5))
        self.F.append(fruit("avocado",510,2))
        self.F.append(fruit("strawberry",60,5))

    def purchase(self,fruitName, shopperName, quantity):
    
        if shopperName.cash >= (fruitName.price*int(quantity)):
            if quantity <= fruitName.quantity:
                return(fruitName.name,str(quantity))
                
            else:
                quantity = fruitName.quantity
                return (fruitName.name,str(quantity))
        else:
            quantity = str(shopper.cash / fruit.price)
            return (fruitName.name, str(quantity))
        #def buy(a,b,c,d):
           #fruit(apple)=fruit(apple)-a
        def get():
            return quantity
class shopper():
    def __init__(self,shopperName,cash,I):
        self.name = shopperName
        self.cash = cash
        # Check....self.FS = fruitstand()
        F = input("") 
        self.FS = fruitstand(F)
        #self.FS.F[2].name
        self.I=[]
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
        for index in (0,len(self.I)):
            if self.I[index].fruitName == self.F.fruitName:
                self.FS.F[index].quantity -= fruitstand.get().quantity
                self.I[index].quantity += quantity
                self.cash = self.cash - fruitName.price * quantity
    def display():
        print(self.shoppeName, self.cash, I,F)
    
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
