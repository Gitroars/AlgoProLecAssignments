class Master:
    #CLASS MODULE
    def __init__(self,name,amount):
        #Gives initial value based on parameter
        self.__name = name
        self.__amount = amount
        #Gives initial value of 0
        self.__staPrice = 0.00
        self.__calPrice = 0.00

   #FUNCTIONS to get the value of an attribute
    def getNameAY(self):
        return self.__name

    def getAmountAY(self):
        return self.__amount

    def getStaPriceAY(self):
        return self.__staPrice

    def getCalPriceAY(self):
        return self.__calPrice

    # A private method which sets the standard price for a child object(item) depending on it's name
    def __PriceListAY(self):
     if self.__name == "Dry Cured Iberian Ham":
        self.__staPrice = 177.80
     elif self.__name == "Wagyu Steaks":
        self.__staPrice = 450.00
     elif self.__name == "Matsutake Mushrooms":
        self.__staPrice = 272.00
     elif self.__name == "Kopi Luwak Coffee":
        self.__staPrice = 306.50
     elif self.__name == "Moose Cheese":
        self.__staPrice = 487.20
     elif self.__name == "White Truffles":
        self.__staPrice = 3600.00
     elif self.__name == "Blue Fin Tuna":
        self.__staPrice = 3603.00
     elif self.__name == "Le Bonnotte Potatoes":
        self.__staPrice = 270.81
     else:
        self.__staPrice = 0.00
     # A public method which calls the private method and modify calculated price (which is 0 by default)
    def CalculateCostAY(self):
     self.__PriceListAY()
     #Calculates using the formula of standard price multiplies by amount
     self.__calPrice = self.__staPrice*self.__amount

    













