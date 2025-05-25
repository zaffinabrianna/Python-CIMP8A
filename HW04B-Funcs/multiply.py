#Multipliation Program
#Brianna Zaffina
#11/13/2023

#Random Module
import random

MY_NAME = "BRIANNA ZAFFINA"

#getData() Function:
def getData():
    randomNum = random.randint(1, 5)
    randomNum2 = random.randint(1, 10)
    return randomNum, randomNum2

#calculate() Function:
def calculate(randNum, randNum2):
    product = randNum * randNum2
    return product

#display() Function:
def display(randNum, randNum2, product):
    print("Integer 1 is:", randNum)
    print("Integer 2 is:", randNum2)
    print(randNum, "times", randNum2, "is equal to", product)
    print()
    print("Program terminated normally")
    
def main():
    print("Multiplication Program -", MY_NAME)
    print()
    #Calling getData() func:
    randNum, randNum2 = getData()
    
    #Calling calculate() func:
    product = calculate(randNum, randNum2)

    #Calling display() func:
    display(randNum, randNum2, product)
    
#Calling main() func:
main()
    
    
