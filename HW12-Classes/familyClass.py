#Family Class Program
#Brianna Zaffina
#12/11/2023

from dataclasses import dataclass

@dataclass
class Family:
    name:str = " "
    address:str = " "
    age:int = 0
    phone:str = " "
    
    def __init__(familyMem, name, address, age, phone):
        familyMem.__name = name
        familyMem.__address = address
        familyMem.__age = age
        familyMem.__phone = phone
        
    #setters:
    def setName(familyMem, name):
        familyMem.__name = name
    def setAddress(familyMem, address):
        familyMem.__address = address
    def setAge(familyMem, age):
        familyMem.__age = age
    def setPhone(familyMem, phone):
        familyMem.__phone = phone

    #getters:
    def getName(familyMem):
        return familyMem.__name
    def getAddress(familyMem):
        return familyMem.__address
    def getAge(familyMem):
        return familyMem.__age
    def getPhone(familyMem):
        return familyMem.__phone

    #display method:
    def display(familyMem, person):
        print("Name:", familyMem.getName())
        print("Address:", familyMem.getAddress())
        print("Age:", familyMem.getAge())
        print("Phone:", familyMem.getPhone())
