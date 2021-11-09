def numAtoms(aG,wE=196.97):
  #constant value for Avogadro's Number
  aN = 6.022*(10**23)
  #Check to see if atomic weight is either of the 3 given elements
  if(wE==196.97):
    print("Gold is selected")
  elif(wE==12.001):
    print("Carbon is selected")
  elif(wE==1.008):
    print("Hydrogen is selected")
  else:
    print("Wrong Input")
    return
  #Calculate mole by dividing atoms(grams) by atomic weight
  moles=aG/wE
  #Calculate number of atoms by multiplying Avogadro's number with moles
  numAtoms=aN*moles
  return numAtoms
  
amountOfElement = int(input("Enter the amount of the element in grams: "))
isSkip = eval(input("Input 0 to enter atomic weight of element\nInput 1 to skip the input of atomic weight of element\n")) #skip input
if(isSkip ==0):
  atomicWeightOfElement = eval(input("Enter the Atomic Weight of Element: "))
  x = numAtoms(amountOfElement,atomicWeightOfElement)
  print(x)
elif(isSkip==1 ):
 x = numAtoms(amountOfElement)
 print(x)
else:
  print("Program Session Ended")