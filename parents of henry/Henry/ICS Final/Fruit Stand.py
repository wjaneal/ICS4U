# -*- coding: utf-8 -*-

class Fruit():
    def __init__(self, name, quantity, price):
        self.name = str(name)
        self.quantity = int(quantity)
        self.price = float(price)

    def getName(self):
        print(self.name)

    def getQuantity(self):
        print(self.quantity)

    def getPrice(self):
        print(self.price)

class Fruitstand():
    def __init__(self):
        self.Orange = Fruit('orange', 100, 1.0)
        self.Mango = Fruit('Mango', 100, 1.5)
        self.Apple = Fruit('Apple', 100, 2.0)
        self.Pear = Fruit('Pear', 100, 2.5)
        self.Banana = Fruit('Banana', 100, 3.0)
        self.list = [self.Orange, self.Mango, self.Apple, self.Pear, self.Banana]

    def purchase(self, shoppername, cash, name, purchasequantity):
        self.name = input('Which fruit do you want to buy:')
        while self.name = Apple or Orange or  Pear or  Banana or  Mango:
            self.quantity = input('How many do you want:")
            while self.quantity >= 0 :
                if cash >= int(purchasequantity) * float(name.price):
                    if name.quantity >= purchasequantity:
                        name.quantity = name.quantity - purchasequantity
                        Newlist = [name, purchasequantity]
                    else:
                        name.quantity = 0
                        Newlist = [name, name.quantity]
                else:
                    purchasequantity = int(cash/name.price)
                    name.quantity = name.quantity - purchasequantity
                    Newlist = [name, purchasequantity]


             return Newlist

    def display(self):
        for i in range (len(self.list)):
            print('NO.', i+1, self.list[i].name, 'Quantity:', self.list[i].quantity)


class Shopper():
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash

        self.Orange = Fruit('orange', 0, 1.0)
        self.Mango = Fruit('Mango', 0, 1.5)
        self.Apple = Fruit('Apple', 0, 2.0)
        self.Pear = Fruit('Pear', 0, 2.5)
        self.Banana = Fruit('Banana', 0, 3.0)
        self.I = [self.Orange, self.Mango, self.Apple, self.Pear, self.Banana]
        self.F = Fruitstand()


    def update(self,name,purchasequantity):

        if name == self.F.Orange:
            print(self.Orange.quantity)
            self.I[0].quantity = self.I[0].quantity + purchasequantity
        if name == self.F.Mango:
            print(self.Mango.quantity)
            self.I[1].quantity = self.I[1].quantity + purchasequantity
        if name == self.F.Apple:
            print(self.Apple.quantity)
            self.I[2].quantity = self.I[2].quantity + purchasequantity
        if name == self.F.Pear:
            print(self.Pear.quantity)
            self.I[3].quantity = self.I[3].quantity + purchasequantity
        if name == self.F.Banana:
            print(self.Banana.quantity)
            self.I[4].quantity = self.I[4].quantity + purchasequantity

        self.I = [self.Orange, self.Mango, self.Apple, self.Pear, self.Banana]
        self.cash = self.cash - int(purchasequantity) * float(name.price)

    def display(self):
        print(self.name, self.cash)
        print("shopper's inventory:")
        for i in range (len(self.I)):
            print(self.I[i].name,self.I[i].quantity)
        print(' ')
        print('Fruit available at the fruit stand:')
        for i in range (len(self.I)):
            print(self.F.list[i].name,self.F.list[i].quantity)

        print(self.name, "'s", 'Money left:', self.cash)

kashun = Shopper('abc',200)
AP = kashun.F.purchase('abc',kashun.cash,kashun.F.Banana,20)
kashun.update(AP[0], AP[1])
kashun.display()
