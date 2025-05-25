#Exception Handling Program
#Brianna Zaffina
#11/27/2023
#This program writes a series of random numbers to a file.
#Each random number should be in the range of 1 through 500.
#The application should let the user specify how many 
#random numbers the file will hold.
import random

#initialize total
total = 0

try:
    num = int(input("How many numbers should the file hold: "))

except ValueError:
    print("A ValueError occured.")
except Exception:
        print("A different error occured.")
    
#open the number.txt file
try:
    with open('numbers.txt', 'w') as numFile:
        #get random numbers
            for count in range(1, num + 1):
                int = random.randint(1, 500)
                print(int)
                #write as a record to the file
                numFile.write(str(int) + '\n')
                total = total + int
except IOError:
    print("A file IOError occured.")
except Exception:
    print("A different error occured.")
    
#print a blank line and other output
try:
    print()
    print(str(num) + ' records written to numbers.txt')
    average = total / num
    print("The total of all numbers written to the file is:", total)
    print("The average of all numbers written to the file is:", average)
except Exception:
    print("A different error occured.")
else:
    print("\nNo exceptions occurred.")
finally:
    print("\nProgram terminated normally.")
