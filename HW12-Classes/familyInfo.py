import familyClass

def main():
    try:
        #First object:
        name, address, age, phone = getData()
        familyMember1 = familyClass.Family(name, address, age, phone)

        #Second object:
        name, address, age, phone = getData()
        familyMember2 = familyClass.Family(name, address, age, phone)

        #Third object:
        name, address, age, phone = getData()
        familyMember3 = familyClass.Family(name, address, age, phone)

        #Display:
        print("\nHere is the first family member entered:")
        familyMember1.display("first")
        print("\nHere is the second family member entered:")
        familyMember2.display("second")
        print("\nHere is the third family member entered:")
        familyMember3.display("third")

        #User Prompt:
        newAge = int(input("\nEnter a new age for the second family member: "))
        familyMember2.setAge(newAge)

        #Re-display:
        print("\nHere is the second family member entered:")
        familyMember2.display("second")

    except ValueError:
        print("/nWrong Data Type")

    except:
        print("\nAnother Error Occurred")

    else:
        print()
        print("Program terminated normally.")

def getData():
    name = str(input("\nEnter the name: "))
    address = str(input("Enter the address: "))
    age = int(input("Enter the age: "))
    phone = str(input("Enter the phone: "))

    return name, address, age, phone

if __name__ == "__main__":
    main()
