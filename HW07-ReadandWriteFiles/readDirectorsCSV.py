#Read Directors from CSV File Program
#Brianna Zaffina
#11/27/2023

import csv

def main():
    print("Read Directors from CSV File")
    print()

    file = "directors.csv"

    with open("directors.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]} ({row[1]})")

    print()
    print("Program terminated normally.")
    
main()
