def calcWeight(w,psg=23.1):
  # Calculate mass by dividing weight on Earth with Earth's surface gravity
  m=w/9.8
  #Calculate effective weight on desired planet by multiplying mass with said planet's surface gravity
  ew=m*psg
  #Prints the effective weight
  return ew

weightOnEarth = eval(input("Weight On Earth:"))
isSkip = eval(input("Input 0 to enter target planet surface gravity\nInput 1 to skip the input of target planet surface gravity\n")) #choose to skip input option
#Checks the value of isSkip to determine whether to give another input,calculate immediately or end the program.
if(isSkip ==0):

  targetPlanetSurfaceGravity = eval(input("Target Planet's Surface Gravity:"))
  print(calcWeight(weightOnEarth,targetPlanetSurfaceGravity))
elif(isSkip==1 ):
 print(calcWeight(weightOnEarth))
else:
  print("Program Session Ended")

