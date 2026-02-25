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
        if guess>=51:
            print("Try between 1-50")
    elif guess < number:
        print("Too Low! Try Again.")
    else:
        print("Congratulations! You guessed the correct number.")
        print("Total Attempts:", attempts)
        break