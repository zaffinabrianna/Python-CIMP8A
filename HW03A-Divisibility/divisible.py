#Divisibility Program
#Brianna Zaffina
#11/6/2023

#1
print("Divisibility Program")
print()

#2
number = (int(input("Enter an integer: ")))

#3 & 4
if number % 5 == 0 and number % 6 == 0:
    print(number, "is divisible by both 5 and 6")

#5 & 6
elif number % 5 == 0 or number % 6 == 0:
    print(number, "is divisible by 5 or 6, but not both")

#7
else:
    print(number, "is NOT divisible by either 5 or 6")

    
 
