from pet import Pet


def displayPet():
    print(f"Name of pet: {myPet.getName()}")
    print(f"Type of pet: {myPet.getType()}")
    print(f"Age of pet: {myPet.getAge()}")
def updatePet():
    print("Let's update the information for a pet!")
    nameOfPet = input("Enter the pet's name: ")
    myPet.setName(nameOfPet)
    typeOfPet = input("Enter the pet's type: ")
    myPet.setType(typeOfPet)
    ageOfPet = int(input("Enter the pet's age: "))
    myPet.setAge(ageOfPet)

print("A pet object has been created. Here is the initial information about the pet: ")
myPet = Pet()
displayPet()
updatePet()
print("Here is the updated information about the pet: ")
displayPet()
