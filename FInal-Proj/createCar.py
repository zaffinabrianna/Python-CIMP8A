import car

def main():
    try:
        print("Car Accelerate and Brake Program - Brianna Zaffina")
        
        #First Object:
        year, make, model, speed = getData()
        car1 = car.Car(year, make, model, speed)

        #Second Object:
        year, make, model, speed = getData()
        car2 = car.Car(year, make, model, speed)

        #Third Object:
        year, make, model, speed = getData()
        car3 = car.Car(year, make, model, speed)

        
        #Display first object:
        print("\nInformation for the first car objcet ...")
        car1.displayDetails("first")

        #first loop:
        for i in range(5):
            car1.accelerate()
            print("After adding 5, the speed is", car1.getSpeed())

        #second loop:
        for i in range(5):
            car1.brake()
            print("After deducting 5, the speed is", car1.getSpeed())

        #Display second object:
        print("\nInformation for the second car object ...")
        car2.displayDetails("second")

        #first loop:
        for i in range(5):
            car2.accelerate()
            print("After adding 5, the speed is", car2.getSpeed())

        #second loop:
        for i in range(5):
            car2.brake()
            print("After deducting 5, the speed is", car2.getSpeed())

        #Display third object:
        print("\nInformation for the third car object ...")
        car2.displayDetails("third")

        #first loop:
        for i in range(5):
            car3.accelerate()
            print("After adding 5, the speed is", car3.getSpeed())

        #second loop:
        for i in range(5):
            car3.brake()
            print("After deducting 5, the speed is", car3.getSpeed())

    except ValueError:
        print("\nWrong data type entered")
        
    except:
        print("\nAnother error occurred")

    else:
        print("\nProgram terminated normally")

def getData():
    year = int(input("\nEnter the year of the car: "))
    make = str(input("Enter the make of the car: "))
    model = str(input("Enter the model of the car: "))
    speed = int(input("Enter the starting speed: "))

    return year, make, model, speed

if __name__ == "__main__":
    main()
