#Inches to Feet Program
#Brianna Zaffina
#11/13/2023

#global consts:
INCHES_IN_FOOT = 12
MY_NAME = "Brianna Zaffina"

#footToInches()
def feetToInches(numOfFeet):
    total = numOfFeet * INCHES_IN_FOOT
    return total
    
#main()
def main():
    total = 0
    print("Convert Feet to Inches Program by", MY_NAME)
    print()
    for i in range(0, 3):
        numOfFeet = float(input("Enter the number of feet in numerics: "))
        total += numOfFeet
        numOfInches = feetToInches(numOfFeet)
        print("There are", numOfInches, "inches in", numOfFeet, "feet.")
        print()
        
    print("The total of values entered by user is", total, ".")
    print()
    print("Program terminated normally")

#call main()
main()


