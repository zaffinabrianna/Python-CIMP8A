#Write Directors to CSV File Program
#Brianna Zaffina
#11/27/2023

import csv

def main():
    print("Write Directors to CSV File")
    print()

    file = "directors.csv"
    
    directors = [["George Lucas", 1944], ["Steven Spielberg", 1946],
                 ["Spike Lee", 1957]]

    with open("directors.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(directors)

    print("Program terminated normally.")

main()
