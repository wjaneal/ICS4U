

#Defines name, price and quantity for a type of fruit
class Fruit:
    
    #This function is known as a class instantiation function
    #It is also known as a constructor
    #The job of a constructor is to make a new instance of a class
    
    def __init__(self,name,price,qut):
        #Here are some class attributes or instance variables
        self.name = name
        self.qut = qut
        self.price = price
        
    def getName(self):
        return self.name
        
    def getPrice(self):
        return self.price
        
    def getQuantity(self):
        return self.qut

#Define fruitstand class
#Defines a list of instances of the fruit class
class fruitsStand:
    def __init__(self, fruitList, fruitPrices, fruitQuantities):
    	#Set up an empty list of fruit
        self.fruitAvailable = []
	#Populate the list with data.
        for i in range(0,len(fruitList)):
            self.fruitAvailable.append(Fruit(fruitList[i],fruitPrices[i],fruitQuantities[i]))
#Define a function to help shoppers buy fruits    
    def purc(self,shopperName,avaCash,fruitName,fruitQuan):
        self.shopperName = shopperName
        self.avaCash = avaCash
        self.fruitName = fruitName
        self.fruitQuan = fruitQuan
        self.frN = ["pear","lemon","apple","grape","cherry"]
        self.fruitIndex = self.frN.index(self.fruitName)
        self.fruQua = self.fruitAvailable[self.fruitIndex].qut
        
        if self.fruitAvailable[self.fruitIndex].qut >= self.fruitQuan and self.avaCash >= self.fruitQuan * self.fruitAvailable[self.fruitIndex].price:
            self.fruQua = self.fruQua - self.fruitQuan
            self.avaCash = self.avaCash - self.fruitQuan * self.fruitAvailable[self.fruitIndex].price

        elif self.avaCash < self.fruitQuan * self.fruitAvailable[self.fruitIndex].price:
            self.fruitQuan = int(self.avaCash / self.fruitAvailable[self.fruitIndex].price)
            self.fruQua = self.fruQua - self.fruitQuan
            self.avaCash = self.avaCash - self.fruitQuan * self.fruitAvailable[self.fruitIndex].price
        '''
        for i in range(0,len(fruitAvailable)):
            while fruitAvailable[i].name == self.fruitName:
                self.num = i
                break
        '''
        if self.fruQua < self.fruitQuan and self.avaCash >= self.fruitQuan * self.fruitAvailable[self.fruitIndex].price:
            self.fruitQuan = self.fruQua
            self.fruQua = 0
            self.avaCash = self.avaCash - self.fruitQuan * self.fruitAvailable[self.fruitIndex].price
        self.record = [self.fruitAvailable[int(self.fruitIndex)].name, self.fruitQuan]
        return self.record
        
#Define a function to help shoppers know what fruits the FruitStand has.           
    def display(self,shopName,fruitQuan):
        print("Fruit Stand has these fruits:")
        for i in range (0, len(self.fruitAvailable)):
            if self.fruitAvailable[i].name == self.fruitName:
                self.fruitAvailable[i].qut = self.fruQua

        for i in range (0, len(self.fruitAvailable)):
            print(str(self.fruitAvailable[i].name)+" "+str(self.fruitAvailable[i].price)+" "+str(self.fruitAvailable[i].qut))
#to get a variable
    def getfr():
        return self.fruitQuan
    '''
    #Define a Sell function for the shopper to sell fruits.
    def sell(self,shopperName,avaCash,fruitName,fruitQuan):
        self.shopperName = shopperName
        self.avaCash = avaCash
        self.fruitName = fruitName
        self.fruitQuan = fruitQuan
        self.frN = ["pear","lemon","apple","grape","cherry"]
        self.fruitIndex = self.frN.index(self.fruitName)
        b = shopper(self.shopperName,self.avaCash)
        self.fruQua2 = self.b.I[self.fruitIndex].qut
        
        if self.fruQua2 >= self.fruitQuan:
            self.fruQua2 = self.fruQua2 - self.fruitQuan
            self.avaCash = self.avaCash + self.fruitQuan * self.fruitAvailable[self.fruitIndex].price

        else:
            self.fruitQuan = self.fruQua2
            self.fruQua2 = 0
            self.avaCash = self.avaCash + self.fruitQuan * self.fruitAvailable[self.fruitIndex].price
        self.record1 = [self.fruitAvailable[int(self.fruitIndex)].name, self.fruitQuan]
        return self.record1
    '''
        
                
        
#define Shopper class       
class shopper:
    def __init__(self,name,money):
        self.name = name
        self.money = money
        self.fN = ["pear","lemon","apple","grape","cherry"]
        self.fP = [1.23,3.54,20.55,5.77,8.82]
        self.fQ = [20,40,60,80,100]

        #Declaration of the fruit stance instance, F
        self.F = fruitsStand(self.fN, self.fP, self.fQ)
        
        self.I = []
        self.I.append(Fruit("pear",0,0))
        self.I.append(Fruit("lemon",0,0))
        self.I.append(Fruit("apple",0,0))
        self.I.append(Fruit("grape",0,0))
        self.I.append(Fruit("cherry",0,0))

#to update the shopper's information        
    def update(self):
        for i in range(0,len(self.I)):
            if self.I[i].name == self.F.fruitName:
                self.I[i].qut = self.F.fruitQuan
                self.F.fruitAvailable[i].qut = self.F.fruitAvailable[i].qut - self.I[i].qut
        self.money = self.F

#Define a function to help shoppers know what fruits he/she has in the beginning.  
    def displayI(self):
        print("Your name:", self.name)
        print("Your money:", self.money)
        print("Dear ", self.name, ",","\nthe fruit stand has these fruits:")
        for i in range(0,len(self.F.fruitAvailable)):
            print(str(self.F.fruitAvailable[i].name)+"   "+str(self.F.fruitAvailable[i].price)+"   "+str(self.F.fruitAvailable[i].qut))
        print("Dear ", self.name, ",","\nyou have fruits:")
        for i in range (0, len(self.I)):
            print(str(self.I[i].name)+" "+str(self.I[i].price)+" "+str(self.I[i].qut))
        
#Define a function to help shoppers know what fruits he/she has after shopping.  
    def display(self):
        print("Your name:", self.name)
        print("Your money:", self.F.avaCash)
        print("Dear ", self.name, ",","\nthe fruit stand has these fruits:")
        for i in range(0,len(self.F.fruitAvailable)):
            print(str(self.F.fruitAvailable[i].name)+"   "+str(self.F.fruitAvailable[i].price)+"   "+str(self.F.fruitAvailable[i].qut))
        print("Dear ", self.name, ",","\nyou have fruits:")
        for i in range (0, len(self.I)):
            print(str(self.I[i].name)+" "+str(self.I[i].price)+" "+str(self.I[i].qut))

            
'''
#input name and money the shopper has.       
n1 = input("Please input your name:")
m1 = int(input("Please input how much money you have:"))
#decide whether you want to buy fruits.
rep = input("Do you want to buy fruits? (y/n)")
#a loop to help the shopper buy fruits.
while rep == "y":
    s = shopper(n1,m1)
    s.displayI()
    #input the fruit name and the quantities.
    f1 = input("What fruits do you want to buy?(pear/lemon/apple/grape/cherry)")
    q1 = int(input("How many fruits do you want to buy?"))
    #a loop to help the FS verify whether the quantity is valid.
    while q1 < 0:
        q1 = int(input("How many fruits do you want to buy?"))
    #calculate the money and fruit.
    s.F.purc(n1,m1,f1,q1)
    #display information of the fruitstand.
    s.F.display(f1,q1)
    #update information of the shopper.
    s.update()
    #ask the shopper whether he/she wants to buy more.
    rep = input("Do you want to continue to buy fruits?(y/n)")
#end, and display information of the shopper
s.display()
print(n1+", thanks for your shopping！")
'''



'''
fN = ["pear","lemon","apple","grape","cherry"]
fP = [1.23,3.54,20.55,5.77,8.82]
fQ = [20,40,60,80,100]

#Declaration of the fruit stance instance, F
F = fruitsStand(fN, fP, fQ)
#Populate the fruit stand with fruit using the data lists.
for i in range(0,len(F.fruitAvailable)):
    print(F.fruitAvailable[i].name+"   "+str(F.fruitAvailable[i].price)+"   "+str(F.fruitAvailable[i].qut))

J = shopper("jack",100)
J.display()
'''
