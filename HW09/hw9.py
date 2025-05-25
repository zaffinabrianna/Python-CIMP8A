# purchase.py
# Brianna Zaffina
# August 4, 2021

# Print titles
print("Purchase Program")
print()
print("=========================")

# Initialize variables
subtotal = 0.0
total = 0.0

# User prompts
price1 = float(input("Enter the price for item 1: "))
price2 = float(input("Enter the price for item 2: "))
price3 = float(input("Enter the price for item 3: "))
price4 = float(input("Enter the price for item 4: "))

# Calculations
subtotal = price1 + price2 + price3 + price4
salesTax = subtotal * 0.08
total = subtotal + salesTax

# Print final output
print()
print(f"{'CATEGORY':10} | {'AMOUNT':10}")
print("=========================")
print(f"{'SUBTOTAL':10} | $ {subtotal:>10,.2f}")
print(f"{'SALES TAX':10} | $ {salesTax:>10,.2f}")
print("=========================")
print(f"{'TOTAL':10} | $ {total:>10,.2f}")
print()
print("Program terminated normally")
