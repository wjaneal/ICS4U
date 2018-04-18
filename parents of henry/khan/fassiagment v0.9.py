# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 13:08:03 2018

@author: simet
"""

class fruit():
    def __init__(self,fruitname,price,quantity):
        self.name = fruitname
        self.price= float(price)
        self.quantity= int(quantity)
    def getName(self):
        print(self.name)
    def getPrice(self):
        print(self.price)
    def getQuantity(self):
        print(self.quantity)
    
class fruitstand():
    def __init__(self):
        self.yasuo,self.orin,self.xerathq=fruit("yasuo",50,10),fruit("orin",100,10),fruit("xerathq",25,9)
        self.fruitlist=[self.yasuo,self.orin,self.xerathq]
    def purchase(self,shoppername,cash,fruitname,purquantity):
        
        if cash>=int(purquantity)*float(fruitname.price):
            if fruitname.quantity>=purquantity:    
                
                fruitname.quantity-=int(purquantity)
                returnlist=[fruitname,fruitname.quantity]
                
                return returnlist
            else:
                print("Fruit not enough in store")
        else:
            print("cash not enough")
    def display(self):
        for i in range (0,2):
            print(self.fruitlist[i].name,self.fruitlist[i].quantity)
        
        
class shopper():
    def __init__(self,name,money):
        self.name=name
        self.cash=money
        self.yasuo,self.orin,self.xerathq=fruit("yasuo",50,0),fruit("orin",100,0),fruit("xerathq",25,0)
        self.I=[self.yasuo,self.orin,self.xerathq]
        self.F=fruitstand()
        self.yasuo.maxquantity=self.F.yasuo.quantity
        self.orin.maxquantity=self.F.orin.quantity
        self.xerathq.maxquantity=self.F.xerathq.quantity
    def update(self,fruitname,fruitquantity):
        if fruitname==self.F.yasuo:
            self.yasuo.quantity=self.yasuo.maxquantity-fruitquantity
            self.cash=self.cash-int(self.yasuo.quantity)*int(self.F.yasuo.price)
        if fruitname==self.F.orin:
            self.orin.quantity=self.orin.maxquantity-fruitquantity
            self.cash=self.cash-int(self.orin.quantity)*int(self.F.orin.price)
        if fruitname==self.F.xerathq:
            self.xerathq.quantity=self.xerathq.maxquantity-fruitquantity
            self.cash=self.cash-int(self.xerathq.quantity)*int(self.F.xerathq.price)
        self.I=[self.yasuo,self.orin,self.xerathq]
    def display(self):
        print(self.name,self.cash)
        for i in range (0,3):
            print(self.I[i].name,self.I[i].quantity)
        for i in range (0,3):
            print(self.F.fruitlist[i].name,self.F.fruitlist[i].quantity)
kalierina=shopper("noone",200)
#kalierina.F.purchase("noone",kalierina.cash,fruitstand.yasuo,1)
k=kalierina.F.purchase("noone",kalierina.cash,kalierina.F.yasuo,2)
kalierina.update(k[0],k[1])
kalierina.display()
        
    
    
        
        
        