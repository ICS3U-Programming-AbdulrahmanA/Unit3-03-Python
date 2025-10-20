#!/usr/bin/env python3
# Created By: Abdul
# Date: 10/20/2025
# Program to ask the user to guess a number between 0 and 9
import random


def main():
    # Get guess from user
    user_guess = float(input("Guess a number between 0-9: "))

    # Calculate computers guess
    computer_guess = random.randint(0, 9)

    # If user guessed correctly or wrongly displayed message
    if user_guess == computer_guess:
        print("You guessed correctly!")
    else:
        print("Wrong! The correct number was", computer_guess)


if __name__ == "__main__":
    main()
