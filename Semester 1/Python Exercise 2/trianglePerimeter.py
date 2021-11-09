edge1 = eval(input("Enter the Length of Edge1 : "))
edge2 = eval(input("Enter the Length of Edge2 : "))
edge3 = eval(input("Enter the Length of Edge3 : "))

sum1= edge1 + edge2
sum2 = edge2 + edge3
sum3 = edge3 + edge1

if (sum1 > edge3) and (sum2 > edge1) and (sum3 > edge2):
    perimeter = edge1 + edge2 + edge3
    print("The perimeter is "+ str(perimeter))
else:
    print("The input is invalid and the perimeter cannot be calculated")
