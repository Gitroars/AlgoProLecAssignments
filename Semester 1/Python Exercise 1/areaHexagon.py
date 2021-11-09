import math

sideLength = eval(input("Enter the side of length of the hexagon : "))

area = round(((3*math.sqrt(3))/2)*pow(sideLength,2),3)

print(f"The area of a hexagon with side length {sideLength} is {area}")
