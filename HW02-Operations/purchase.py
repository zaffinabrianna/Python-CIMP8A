# HW2 (purhase.py)
# Brianna Zaffina
# 10/30/23

# Printing the title:
print("Purchase Program")
print()
print("=========================")

#Init Variables:
subtotal = 0.0
total = 0.0

#User Prompt and Subtotal:
price1 = (float(input("Enter the price for item 1: ")))
subtotal += price1
price2 = (float(input("Enter the price for item 2: ")))
subtotal += price2
price3 = (float(input("Enter the price for item 3: ")))
subtotal += price3
price4 = (float(input("Enter the price for item 4: ")))
subtotal += price4

#Calculations:
salesTax = subtotal * 0.08
total = subtotal + salesTax

#Round two places to the decimal:
subtotal = round(subtotal, 2)
salesTax = round(salesTax, 2)
total = round(total, 2)

#Output:
print("=========================")
print("SUBTOTAL:   $", subtotal)
print("SALES TAX:  $ ", salesTax)
print("TOTAL:      $", total)

print()
print("Program terminated normally")

