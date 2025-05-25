#Car Accelerate and Brake Program
#Brianna Zaffina
#12/18/23

from dataclasses import dataclass

@dataclass
class Car:
    #private variables:
    year:int = 0
    make:str = " "
    model:str = " "
    speed:int = 0

    def __init__(car, year, make, model, speed):
        car.__year = year
        car.__make = make
        car.__model = model
        car.__speed = speed

    def accelerate(car):
        car.__speed = car.__speed + 5

    def brake(car):
        car.__speed = car.__speed - 5;

    #getters:
    def getYear(car):
        return car.__year
    def getMake(car):
        return car.__make
    def getModel(car):
        return car.__model
    def getSpeed(car):
        return car.__speed

    #setters
    def setYear(car, year):
        car.__year = year
    def setMake(car, make):
        car.__make = make
    def setModel(car, model):
        car.__model = model
    def setSpeed(car, speed):
        car.__speed = speed

    #Display Method:
    def displayDetails(car, acar):
        print("Year:\t\t", car.getYear())
        print("Make:\t\t", car.getMake())
        print("Model:\t\t", car.getModel())
        print("Speed\t\t", car.getSpeed())
        
