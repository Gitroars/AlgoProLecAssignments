
from foodParentAY import Master #imports the class from the other script

def CreateListObjectsAY():
    li=[] #an empty list
    numberOfItems = int(input("Enter the number of items: "))
    while numberOfItems<=0: #Verify if number of items is more than 1
        print("Number of items must be at least 1.") #Warn the user for correct input
        numberOfItems = int(input("Enter the number of items: ")) #Allows the user to input again
    if numberOfItems >=1:
        for x in range(numberOfItems):
            print(f"Item #{x+1}") #Order number
            name = input("Enter food:")
            amount = float(input("Enter amount of pounds:"))
            while amount <= 0:
                print('Amount of pounds must be greater than 0.')
                amount = float(input("Enter amount of pounds:"))
            child = Master(name,amount)
            Master.CalculateCostAY(child)
            li.append(child) #Adds the newly created object to the list
        return li


def DisplayContentAY(list):
    print("Here's a summary of the items purchased: \n ----------------------------------------------------------------")
    x=0
    while x<len(list):
        print("Item: ",list[x].getNameAY())
        print(f"Amount ordered: {list[x].getAmountAY()} pounds")
        print(f"Price per pound: ${list[x].getStaPriceAY():.2f}")
        print(f"Price of order: ${list[x].getCalPriceAY():.2f} \n")
        x+=1

def CalculateTotalCostAY(list):
    totalCost = 0
    i = 0
    while i<len(list):
        totalCost += list[i].getCalPriceAY()
        i+=1

    return totalCost


def main():
    myList = CreateListObjectsAY()
    DisplayContentAY(myList)
    myTotalCost = CalculateTotalCostAY(myList)
    print(f"Total Cost: ${myTotalCost:.2f}")

main() #Call the functions



