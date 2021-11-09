subtotal = eval(input("Enter the subtotal:$"))
gratuity = eval(input("Enter the tip amount (as a %):"))

tip = subtotal + ((gratuity/100)*subtotal)
total = subtotal + tip

subtotal = '{0:,.2f}'.format(subtotal)
tip = '{0:,.2f}'.format(tip)
total = '{0:,.2f}'.format(total)

print(f"Subtotal:${subtotal}")
print(f"Tip:${tip}")
print(f"Total:${total}")
