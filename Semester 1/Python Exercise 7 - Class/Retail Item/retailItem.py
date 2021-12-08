class Retail_Item:
    def __init__(self, type, amount, price):
        self.__type = type
        self.__amount = amount
        self.__price = price
    def setName(self, name):
        self.__name = name

    def setAmount(self, amount):
        self.__type = amount

    def setPrice(self, price):
        self.__age = price

    def getName(self):
        return self.__name

    def getAmount(self):
        return self.__amount

    def getPrice(self):
        return self.__price
    def __str__(self):
        return "Name of item:{} Amount of item:{} Price of item:{}".format(self.getName(), self.getType(), self.getPrice())
