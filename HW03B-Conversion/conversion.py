# C to F Conversion Program
# Brianna Zaffina
# 11/6/2023

#Printing Title
print("Celsius to Fahrenheit Conversion Program")
print()

#Set Varibles
celsius = 0

#Print Table Headings
print("CELSIUS", "\t", "FAHRENHEIT")
print("=======", "\t", "==========")

#For loop from 0 - 20 that prints C and its conversion to F
for celsius in range(0, 21):
    print(celsius, "\t\t", round((((9/5) * celsius) + 32), 1))
