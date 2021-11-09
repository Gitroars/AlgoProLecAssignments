def calculateNewHeight():
  #Input current width and height
  currentWidth=eval(input("Enter the current width: "))
  currentHeight=eval(input("Enter the current height: "))
  #Calculate aspect ratio of x by dividing current width with current height
  aspectRatioX=currentWidth/currentHeight
  #Input the desired width
  newWidth=eval(input("Enter the desired width: "))
  #Calculate new height according to desired width
  newHeight=float(newWidth/aspectRatioX)
  print("New height is ", newHeight)

  return newHeight

x=calculateNewHeight()