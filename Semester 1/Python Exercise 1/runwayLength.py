speed = eval(input("Enter the plane's take off speed in m/s : "))
acceleration = eval(input("Enter the plane's acceleration in m/s**2 : "))
minRunwayLength = (speed**2)/(2*acceleration)
print(f"The minimum runway length needed for this airplane is {round(minRunwayLength,4)}")