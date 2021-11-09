integer = int(input("Input an integer value : "))
output = ""

if integer%11 == 0:
    output += "a"
if integer%9 == 0:
    output += "b"
if integer%7 == 0:
    output += "c"
if integer%2 == 0:
    output += "d"
if output == "":
    output = "e"
print(output)
