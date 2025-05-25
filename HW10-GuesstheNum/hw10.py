# guess_the_numberNew.py
# Brianna Zaffina
# 4 December 2023

import random

LIMIT = 10

def display_title():
    print("Guess the number!")
    print()

def play_game():    
    number = random.randint(1, LIMIT)
    print("I'm thinking of a number from 1 to " + str(LIMIT) + "\n")
    count = 1
    guess = LIMIT + 1
    while guess != number:
        guess = (input("Your guess: "))
        
        if guess.isdigit():
            guess = int(guess)
            
            if guess < number:
                print("Too low.")
                count += 1
            elif guess > number:
                print("Too high.")
                count += 1
            elif guess == number:
                print("You guessed it in " + str(count) + " tries.\n")
                
        else:
            print("Invalid input -- numeric digits only -- try again!")

def main():
    display_title()
    again = "y"
    while again.lower() == "y":
        play_game()
        again = input("Would you like to play again? (y/n): ")
        print()
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

