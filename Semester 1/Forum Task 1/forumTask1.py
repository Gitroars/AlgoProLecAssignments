import math

numerator = int(input("Enter a numerator : "))
while(numerator < 1):
    print("The value of the input must be greater than 0")
    numerator = int(input("Re-enter a numerator : "))

denominator = int(input("Enter a denominator : "))
while(denominator < 1):
    print("The value of the input must be greater than 0")
    denominator = int(input("Re-enter a denominator : "))

gcd = math.gcd(numerator, denominator)

if numerator<denominator:
    print(f"{numerator}/{denominator} is a proper fraction")
    if gcd == 1: print("The proper fraction can't be reduced")
    elif gcd !=1:
        numerator //= gcd
        denominator //= gcd
        print(f"This proper fraction can be reduced to : {numerator}/{denominator}")
elif numerator>=denominator:
    print(f"{numerator}/{denominator} is an improper fraction")
    if gcd == 1: print("The improper fraction can't be reduced")
    elif gcd !=1:
        numerator //= gcd
        denominator //= gcd
        print(f"This improper fraction can be reduced to : {numerator}/{denominator}")
    wholeNumber = numerator//denominator
    remainder = numerator%denominator
    if remainder != 0:
        print(f"The mixed number is {wholeNumber} and {remainder}/{denominator}")
    elif remainder == 0:
        print(f"The whole number is {wholeNumber}")
