# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 11:02:02 2018

@author: xuyin
"""

class fruit():
    def __init__(self,fruitname,quantity,price):
        self.name = str(fruitname)
        self.price = float(price)
        self.quantity = int(quantity)
        
    def getName(self):
        print(self.name)
        
    def getPrice(self):
        print(self.price)
        
    def getQuantity(self):
        print(self.quantity)

class fruitstand():
    def __init__(self):
        self.Apple, self.Banana, self.Pear, self.Grape, self.Pineapple = fruit('Apple',100,2),fruit('Banana',300,3),fruit('Pear',300,1),fruit('Grape',100,3),fruit('Pineapple',200,10)
        self.fruitList = [self.Apple, self.Banana, self.Pear, self.Grape, self.Pineapple]

    def purchase(self,shoppername,money,fruitname,purchasequantity):
        if money>=purchasequantity*fruitname.price:
            if fruitname.quantity>=purchasequantity:
                fruitname.quantity-=purchasequantity
                returnlist=[fruitname,purchasequantity]
            else:
                purchasequantity=fruitname.quantity
                fruitname.quantity-=purchasequantity
                returnlist=[fruitname,purchasequantity]
        else:
            purchasequantity= int(money // fruitname.price)
            returnlist=[fruitname,purchasequantity]
        print(returnlist)
        return returnlist
    
    def sell(self,shoppername,money,fruitname,sellquantity):
        if money>=sellquantity*fruitname.price:
            if fruitname.quantity>=sellquantity:
                fruitname.quantity-=sellquantity
                returnlist2=[fruitname,sellquantity]
            else:
                sellquantity=fruitname.quantity
                fruitname.quantity-=sellquantity
                returnlist2=[fruitname,sellquantity]
        else:
            sellquantity= int(money // fruitname.price)
            returnlist=[fruitname,sellquantity]
        print(returnlist2)
        return returnlist2
    
    def display(self):
        for i in range (0,len(self.fruitList)):
            print(self.fruitList[i].name,self.fruitList[i].quantity)

        
class shopper():
    def __init__(self,shoppername,money):
        self.shoppername = shoppername
        self.money = money
        self.F = fruitstand()
        self.Apple, self.Banana, self.Pear, self.Grape, self.Pineapple = fruit('Apple',0,2),fruit('Banana',0,3),fruit('Pear',0,1),fruit('Grape',0,3),fruit('Pineapple',0,10)
        self.I = [self.Apple, self.Banana, self.Pear, self.Grape, self.Pineapple]
        
    def update(self, fruitname, purchasequantity):
        self.quantity=purchasequantity
        if fruitname==self.F.Apple:
            self.I[0].quantity+=purchasequantity
            self.money=self.money-self.Apple.quantity*self.F.Apple.price
        if fruitname==self.F.Banana:
            self.I[1].quantity+=purchasequantity
            self.money=self.money-self.Banana.quantity*self.F.Banana.price
        if fruitname==self.F.Pear:
            self.I[2].quantity+=purchasequantity
            self.money=self.money-self.Pear.quantity*self.F.Pear.price
        if fruitname==self.F.Grape:
            self.I[3].quantity+=purchasequantity
            self.money=self.money-self.Grape.quantity*self.F.Grape.price
        if fruitname==self.F.Pineapple:
            self.I[4].quantity+=purchasequantity
            self.money=self.money-self.Pineapple.quantity*self.F.Pineapple.price
            
        self.I[2].quantity+=5 #This could add 5 pears to the shopper's inventory
        self.I = [self.Apple, self.Banana, self.Pear, self.Grape, self.Pineapple]
        
    def display(self):
        print(self.shoppername,self.money)
        print("fruit in the store")
        for i in range (0,len(self.I)):
            print(self.F.fruitList[i].name,self.F.fruitList[i].quantity)
        print("shopper's information")
        for i in range (0,len(self.I)):
            print(self.I[i].name,self.I[i].quantity)
        print('Thank you for shopping!') #This thanks the shopper
    
    def fruitindex (self, fruitname): # PartB
        for i in range (0,5):
            if self.F.fruitList[i].name == fruitname:
                print (self.F.fruitList[i].name,self.F.fruitList[i].quantity,self.F.fruitList[i].price)
                
    def check (self): #This checks whether the shopper has enough money to buy 5 bananas
        if self.money >= 5 * self.F.Banana.price:
            print('You have enough money!')
        else:
            print("You don't have enough money!")
    

Mike=shopper("b",200)
c=Mike.F.purchase('b',Mike.money,Mike.F.Apple,20)
Mike.update(c[0],c[1])
Mike.display()
Mike.fruitindex('Apple')#Check if he could afford --> PartB
Mike.check()

a = str(input('Do you what to stop? Please write Yes or No: '))
while a == 'No':
    if str(input('Do you want apple(Yes or No)')) == 'Yes': #Quesion1 c
        i = 0
    if str(input('Do you want banana(Yes or No)')) == 'Yes': #Quesion1 c
        i = 1
    if str(input('Do you want pear(Yes or No)')) == 'Yes': #Quesion1 c
        i = 2
    if str(input('Do you want grape(Yes or No)')) == 'Yes': #Quesion1 c
        i = 3
    if str(input('Do you want pineapple(Yes or No)')) == 'Yes': #Quesion1 c
        i = 4
    
    number = int(str(input('How many fruits do you want?'))) #Question1 d
    Mike=shopper("b",200)
    c=Mike.F.purchase('b',Mike.money,Mike.F.fruitList[i],number)
    Mike.update(c[0],c[1])
    Mike.display() #Question 1 b
    Mike.fruitindex('Apple') # Check if he could buy
    Mike.check()
    a = str(input('Do you what to stop? Please write Yes or No: '))
    

    
