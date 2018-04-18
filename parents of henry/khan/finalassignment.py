# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 13:08:03 2018

@author: simet
"""

class fruit():#creat a class
    def __init__(self,fruitname,price,quantity):#get the three variables
        self.name = fruitname#make a class variable
        self.price= int(price)#make another class variable
        self.quantity= int(quantity)#make another class variable
    def getName(self):#def three fuctions
        print(self.name)#print the name
    def getPrice(self):
        print(self.price)#print the price
    def getQuantity(self):
        print(self.quantity)#print the quantity of the fruit
    
class fruitstand():#creat a class
    def __init__(self):#creat 5 fruit incidences
        self.yasuo,self.orin,self.xerathq,self.kaz,self.lux=fruit("yasuo",50,10),fruit("orin",100,10),fruit("xerathq",25,9),fruit("kaz",25,10),fruit("lux",25,10)
        self.fruitlist=[self.yasuo,self.orin,self.xerathq,self.kaz,self.lux]#creat a fruitlist
    def purchase(self,shoppername,cash,fruitname,purquantity):#creat a purchase function
        if cash>=int(purquantity)*float(fruitname.price):#determine the situation
            if fruitname.quantity>=purquantity:#when there is enough money and fruit
                fruitname.quantity-=purquantity
                returnlist=[fruitname,purquantity]#creat returnlist
            else:#there is enough money but not enough fruit
                purquantity=fruitname.quantity
                fruitname.quantity-=purquantity
                returnlist=[fruitname,purquantity]#creat returnlist
        else:
            #there is not enough money
            purquantity=min(int(int(cash)/int(fruitname.price)),fruitname.quantity)#to determine what amount of fruit can be bought
            fruitname.quantity-=purquantity
            returnlist=[fruitname,purquantity]#returnlist
            
        return returnlist# return the returnlist
    def display(self):#creat the display function
        print("fruit available:")
        for i in range (0,len(self.fruitlist)):#repeat the print
            print(self.fruitlist[i].name,self.fruitlist[i].quantity)#show the name and quantity of fruit available


class shopper():#creat a neew class
    def __init__(self,name,money):#get the name and money
        self.name=name
        self.cash=money
        #creat 5 fruit incidences
        self.yasuo,self.orin,self.xerathq,self.kaz,self.lux=fruit("yasuo",50,0),fruit("orin",100,0),fruit("xerathq",25,0),fruit("kaz",25,0),fruit("lux",25,0)
        #creat the inventory
        self.I=[self.yasuo,self.orin,self.xerathq,self.kaz,self.lux]
        #creat a incidence of fruitstand
        self.F=fruitstand()

        
        
    def update(self,fruitname,purquantity):#creat a update function
        self.purquantity=purquantity
        if fruitname==self.F.yasuo:#determine which fruit is bought
            
            self.yasuo.quantity+=purquantity#change the fruit amount in the inventory
            self.cash=self.cash-int(self.yasuo.quantity)*int(self.F.yasuo.price)#change the cash due to the purchase
        if fruitname==self.F.orin:
            self.orin.quantity+=purquantity
            self.cash=self.cash-int(self.orin.quantity)*int(self.F.orin.price)
        if fruitname==self.F.xerathq:
            self.xerathq.quantity+=purquantity
            self.cash=self.cash-int(self.xerathq.quantity)*int(self.F.xerathq.price)
        if fruitname==self.F.kaz:
            self.kaz.quantity+=purquantity
            self.cash=self.cash-int(self.kaz.quantity)*int(self.F.kaz.price)        
        if fruitname==self.F.lux:
            self.lux.quantity+=purquantity
            self.cash=self.cash-int(self.lux.quantity)*int(self.F.lux.price)        
        self.I=[self.yasuo,self.orin,self.xerathq,self.kaz,self.lux]
    def display(self):#creat the display function
        print(self.name,self.cash)#show the name of the shopper and his or her cash
        print("fruit in bag")
        for i in range (0,len(self.I)):#show the fruit names and quantities in the inventory
            print(self.I[i].name,self.I[i].quantity)
        print("fruit seen in the store")
        for i in range (0,len(self.I)):#show the fruit names and quantities in the fruitstand
            
            print(self.F.fruitlist[i].name,self.F.fruitlist[i].quantity)
kalierina=shopper("noone",200)#creat a shopper
k=kalierina.F.purchase("noone",kalierina.cash,kalierina.F.yasuo,5)#let the shopper buy 5 yasuo
kalierina.update(k[0],k[1])#update the information
kalierina.display()
kalierina.F.display()
    
