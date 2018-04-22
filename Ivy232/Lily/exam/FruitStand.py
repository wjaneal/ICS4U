
class fruit:
    def __init__(self, name, price, quantity):
        self.name = name #Pass a variable name.
        self.price = price #Pass a variable name.
        self.quantity = quantity #Pass a variable name.

    def getName(self):
        print(self.name) #Print the variable self.name

    def getPrice(self):
        print('%s:%s' % (self.fruitName, self.price)) #Print the variable self.price

    def getQuantity(self):
        print(self.quantity) #Print the variable self.quantity

class fruitStand:
    def __init__(self, fruitName, fruitPrice, fruitQuantity):

        self.fruitAvailable = [] #Prepare an empty list for instances of fruit with name, price and quantity.
        self.fruitAvailable.append(fruit("banana", 2.4, 23))
        self.fruitAvailable.append(fruit("durian", 11.2, 13))
        self.fruitAvailable.append(fruit("mango", 7.3, 18))
        self.fruitAvailable.append(fruit("pineapple", 7.7, 56))
        self.fruitAvailable.append(fruit("kiwi", 5.3, 43))
        #for i in range (0, len(fruitName)):
            #self.fruitAvailable.append(fruit(fruitName[i], fruitPrice[i], fruitQuantity[i])) #why here add "fruit"?
            #Create instances of "fruit" class, and organize them into the list called "fruitAvailable" in "fruitStand" class.

    def purchase(self, shopperName, availableCash, FruitName, FruitQuantity):
        self.FruitQuantity = FruitQuantity
        self.availableCash = availableCash
        self.FruitName = FruitName
        self.shopperName = shopperName
        self.fN = ["banana", "durian", "mango", "pineapple", "kiwi" ]
        self.fruitIndex = self.fN.index(self.FruitName)
        self.QuantityNow = self.fruitAvailable[self.fruitIndex].quantity
        #Get the index of the fruit that the shopper wants to buy in the list. Thus the type of fruit can be found in the list "fruitAvailable". 
        #self.fruit = self.fruitAvailable[int(self.fruitIndex)][0]
        
        if self.QuantityNow >= self.FruitQuantity and self.FruitQuantity * self.fruitAvailable[int(self.fruitIndex)].price <= self.availableCash:
            #When the total quantity of certain fruit can satisfy the shopper, and the shopper has enough money,
            
            self.QuantityNow = self.QuantityNow - self.FruitQuantity
            #the amount of certain fruit will change according to the purchase, directly.

            self.availableCash = self.availableCash - self.FruitQuantity * self.fruitAvailable[int(self.fruitIndex)].price
        
        elif self.FruitQuantity * self.fruitAvailable[self.fruitIndex].price > self.availableCash:
            #When the total quantity of certain fruit is too expensive for the shopper,
            
            self.max = self.availableCash/self.fruitAvailable[self.fruitIndex].price
            #the shopper can only get as much fruit as he can according to the money he has.

 
            
            self.FruitQuantity = int(self.max)
            #Convert the decimal into integer.

            self.QuantityNow = self.QuantityNow - self.FruitQuantity

            self.availableCash = self.availableCash - self.FruitQuantity * self.fruitAvailable[int(self.fruitIndex)].price
  
        elif self.QuantityNow < self.FruitQuantity and self.FruitQuantity * self.fruitAvailable[int(self.fruitIndex)].price <= self.availableCash:
            #When the total quantity of certain fruit cannot satisfy the shopper, and the shopper has enough money,
            self.FruitQuantity = self.QuantityNow
            #the shopper will buy all the fruit available at the fruit stand.
            self.QuantityNow = 0
            self.availableCash = self.availableCash - self.FruitQuantity * self.fruitAvailable[int(self.fruitIndex)].price
        self.note = [self.fruitAvailable[int(self.fruitIndex)].name, self.FruitQuantity]
        self.sell = [self.fruitAvailable[int(self.fruitIndex)].name, self.FruitQuantity]
        #This is the info about the purchase, in the form of a list with two elements -- name of fruit and quantity of fruit purchased.
        return self.note, self.sell

        
    def display(self):
        
          
        for i in range (0, len(self.fruitAvailable)):
            if self.fruitAvailable[i].name == self.FruitName:
                self.fruitAvailable[i].quantity = self.QuantityNow

        for i in range (0, len(self.fruitAvailable)):
            print(str(self.fruitAvailable[i].name)+" "+str(self.fruitAvailable[i].price)+" "+str(self.fruitAvailable[i].quantity))
                   

class shopper:
    def __init__(self, shopperName, money):
        self.shopperName = shopperName #Pass a variable name.
        self.money = money #Pass a variable name.
        '''
        self.FS = fruitstand()
        FS
        
        self.fN = ["banana", "durian", "mango", "pineapple", "kiwi" ]
        self.fP = [2.4, 11.2, 7.3, 7.7, 5.3]
        self.fQ = [23, 13, 18, 56, 43]
        '''

        self.F = fruitStand(0,0,0)
        #self.I = [["banana", 0],["durian", 0],["mango", 0],["pineapple", 0],["kiwi", 0]]
        self.I = []
        self.I.append(fruit("banana", 0, 0))
        self.I.append(fruit("durian", 0, 0))
        self.I.append(fruit("mango", 0, 0))
        self.I.append(fruit("pineapple", 0, 0))
        self.I.append(fruit("kiwi", 0, 0))
        
        

    def update(self):
        for i in range (0, len(self.I)):
            if self.I[i].name == self.F.FruitName:
                self.I[i].quantity = self.F.FruitQuantity
                self.F.fruitAvailable[i].quantity = self.F.QuantityNow

        self.money = self.F.availableCash
        
            
                
                

    def display(self):
        print("###############RECIEPT####################")
        print("Name:" + self.shopperName)
        
        print("Available cash:" + str(self.money))
        print("##########################################")        

        print("Dear " + self.shopperName + "," + "\nthe current fruit list of the fruit stand is shown below:")
        for i in range (0, len(self.F.fruitAvailable)):
            print(str(self.F.fruitAvailable[i].name)+" "+str(self.F.fruitAvailable[i].price)+" "+str(self.F.fruitAvailable[i].quantity))
        
        print("\nYour current inventory is shown below:")
        for i in range (0, len(self.I)):
            print(str(self.I[i].name)+" "+str(self.I[i].price)+" "+str(self.I[i].quantity))
        


   
fN = ["banana", "durian", "mango", "pineapple", "kiwi" ]


while True:
    shopperAName = input("Please enter your name:")
    shopperAMoney = float(input("Please enter the money you have:"))
    while shopperAMoney < 0:
        shopperAMoney = float(input("Please enter a positive number for the cash you have:"))
        
    shopperAfruit = input("Please enter the fruit you want:")
    while shopperAfruit not in fN:
        shopperAfruit = input("Please enter the crect fruit name:")

    shopperAquantity = float(input("Please enter the quantity of fruit you want:"))
    while int(shopperAquantity) != shopperAquantity or shopperAquantity < 0:
        shopperAquantity = float(input("Please enter a positive integer for the quantity:"))

    FF = shopper(shopperAName, shopperAMoney)

    
    
    FF.F.purchase(shopperAName, shopperAMoney, shopperAfruit, shopperAquantity)
    FF.F.display()
    FF.update()

    

    request = input("Do you want to continue? (If you do, please enter  YES  )")
    if request != "YES":
        break
    
FF.display()
print("Thank you for your purchase! Have a good day!")



def fruitindex(x):
    
    for i in range (0, len(FF.F.fruitAvailable)):
        if x == FF.F.fruitAvailable[i].name:
            return i
        
q=fruitindex(input("The fruit name:"))
print(q)
m=int(q)
print("The shopper has " + str(FF.I[m].quantity) + " " + str(FF.F.fruitAvailable[m].name) + "s")

FF.F.availableCash >= 5*FF.F.fruitAvailable[m].quantity

FF.I[m].quantity = FF.I[m].quantity + 5



'''
shopperA = shopper(input(""),input(""))
shopper.conduction
'''




#S = shopper()
#S.FS
#F = fruitStand(fN, fP, fQ)
#FPrint = fruit(fN, fP, fQ)
#FPrint.getName()
#FPrint.getPrice()
#FPrint.getQuantity()

    #What is the list fruitAvailable exactly?

#quantity,
#get price
#

