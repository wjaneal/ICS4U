class fruit:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def getName(self):
        return self.name

    def getQuantity(self):
        return self.quantity

    def getPrice(self):
        return self.price


class fruitstand:
    def __init__(self):
        self.fruits = [
                fruit("apple", 5, 2), 
                fruit("bananas", 20, 3), 
                fruit("pears", 20, 1.5), 
                ]

    def purchase(self, name_of_shopper, cash, 
            name_of_fruit, quantity):
        for item in self.fruits:
            if item.getName() == name_of_fruit:
                num_of_fruit = 0
                while True:
                    cash -= item.getPrice()
                    quantity -= 1
                    if cash >= 0 and quantity >= 0:
                        num_of_fruit += 1
                        item.quantity -= 1
                    else:
                        break

                return [item.getName(), num_of_fruit]                                   

    def display(self):
        print("fruitstand:")
        for item in self.fruits:
            print("{}\t{}\t\n".format(item.getName(), 
                item.getQuantity()))


class shopper:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.F = fruitstand()
        self.I = [
                fruit("apple", 0, 2), 
                fruit("bananas", 0, 3), 
                fruit("pears", 0, 1.5), 
                ]

    def update(self, name_of_fruit, quantity):
        income = self.F.purchase(self.name, self.money, 
                name_of_fruit, quantity)
        for item in self.I:
            if item.getName() == income[0]:
                item.quantity += income[1]

    def display(self):
        print("shoper's name: {}\t\nshoper's money: {}\t\n"
                .format(self.name, self.money))
        for item in self.I:
            print("{}\t{}\t\n".format(item.getName(), 
                item.getQuantity()))
        self.F.display()

if __name__ == "__main__":
    s = shopper("c", 20)
    s.update("apple", 2)
    s.display()
