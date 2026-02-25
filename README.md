📖 Overview

This is a simple interactive Python game where:

The computer generates a random number between 1 and 50

The user tries to guess the correct number

The program provides hints (Too High / Too Low)

Total attempts are counted

🎯 Objective

To demonstrate:

Loops

Conditional statements

Random number generation

User interaction

💻 Code
import random

number = random.randint(1, 50)
attempts = 0

print("NUMBER GUESSING GAME")
print("Guess a number between 1 and 50")

while True:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess > number:
        print("Too High! Try Again.")
        if guess >= 51:
            print("Try between 1-50")
    elif guess < number:
        print("Too Low! Try Again.")
    else:
        print("Congratulations! You guessed the correct number.")
        print("Total Attempts:", attempts)
        break
▶️ Example Output
NUMBER GUESSING GAME
Guess a number between 1 and 50
Enter your guess: 25
Too Low! Try Again.
Enter your guess: 40
Too High! Try Again.
Enter your guess: 33
Congratulations! You guessed the correct number.
Total Attempts: 3
📚 Concepts Used

Random Module

While Loop

Conditional Logic

Counters

User Input

👩‍💻 Author

Subasri A
B.E CSE (Cyber Security)# number-guessing-game-python
A Python console-based number guessing game where the user guesses a randomly generated number between 1 and 50.
