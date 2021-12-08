
from foodParentAY import Master #imports the class from the other script

def CreateListObjectsAY():
    li=[] #an empty list
    numberOfItems = int(input("Enter the number of items: "))
    while numberOfItems<=0: #Verify if number of items is more than 0
        print("Number of items must be at least 1.") #Warn the user for correct input
        numberOfItems = int(input("Enter the number of items: ")) #Allows the user to input again
    if numberOfItems >=1: #Verify if number of items is at least 1
        for x in range(numberOfItems): #For every time,
            print(f"Item #{x+1}") #print the item order number
            name = input("Enter food: ")
            amount = float(input("Enter amount of pounds: "))
            while amount <= 0: #Verify if amount of pounds is not greater than 0
                print('Amount of pounds must be greater than 0.') #Warns the user for correct input
                amount = float(input("Enter amount of pounds:")) #Allows the user to input again
            child = Master(name,amount) #Creates a new child object using user's input data
            Master.CalculateCostAY(child) #Calculate the cost of the recently created object
            li.append(child) #Adds the newly created object to the list
        return li #gives the value to the global list


def DisplayContentAY(list): #Summary for Items Purchased
    print("Here's a summary of the items purchased: \n ----------------------------------------------------------------")
    x=0 #index
    while x<len(list): #For every item,
        print("Item: ",list[x].getNameAY()) #prints the name
        print(f"Amount ordered: {list[x].getAmountAY()} pounds") #prints the amount
        print(f"Price per pound: ${list[x].getStaPriceAY():.2f}") #prints the price per pound with 2 decimals
        print(f"Price of order: ${list[x].getCalPriceAY():.2f} \n") #prints the price order with 2 decimals
        x+=1

def CalculateTotalCostAY(list):
    totalCost = 0 #declare the local total cost with the value of 0
    i = 0 #index
    while i<len(list): #at every item,
        totalCost += list[i].getCalPriceAY() #increase total cost by the calculated price
        i+=1

    return totalCost #gives the value to the global totalCost


def main():
    myList = CreateListObjectsAY() #declare a list using a function which creates a new list composed of objects
    DisplayContentAY(myList) #prints the content of the list said beforehand
    myTotalCost = CalculateTotalCostAY(myList) #declare the total cost using a function
    print(f"Total Cost: ${myTotalCost:.2f}") #prints the total cost with 2 decimals

main() #Call the functions



