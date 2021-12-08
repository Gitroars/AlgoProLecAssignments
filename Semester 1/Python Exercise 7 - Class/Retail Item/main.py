from retailItem import Retail_Item


# def main():
#  nameOfItem1 = input("Name of item 1: ")
#  amountOfItem1 = int(input("Amount of item 1: "))
#  priceOfItem1 = float(input("Price of item 1: "))
#
#  nameOfItem2 = input("Name of item 2: ")
#  amountOfItem2 = int(input("Amount of item 2: "))
#  priceOfItem2 = float(input("Price of item 2: "))
#
#  item1 = Retail_Item(nameOfItem1,amountOfItem1,priceOfItem1)
#  item2 = Retail_Item(nameOfItem2,amountOfItem2,priceOfItem2)
li=[]
x = int(input("How many items to input? "))
for i in range(x):
 nameOfItem = input("Name of item : ")
 amountOfItem = int(input("Amount of item : "))
 priceOfItem = float(input("Price of item : "))
 li.append(Retail_Item(nameOfItem,amountOfItem,priceOfItem))
for i in range(x):
 print(li[x])




