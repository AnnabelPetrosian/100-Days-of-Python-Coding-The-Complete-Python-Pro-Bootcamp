import random
from art import logo

print(logo)

print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1, 100)
print(random_number)
level_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
easy = 10
hard = 5
your_guess = 0


def make_guess():
    global your_guess
    your_guess = int(input("Make a guess: "))


def checking_number():
    if your_guess > random_number:
        print("Too high. ")
    elif your_guess < random_number:
        print("Too low. ")
    else:
        print(f"You guessed it!!! The number was {random_number}. ")
        exit()
    print("Guess again. ")
    

if level_difficulty == "easy":
    for n in range(0, easy):
        print(f"You have {easy} attempts remaining to guess the number")
        make_guess()
        checking_number()
        easy -= 1
    if easy == 0:
        print("You've run out of guesses, you lose. ")


if level_difficulty == "hard":
    for n in range(0, hard):
        print(f"You have {hard} attempts remaining to guess the number")
        make_guess()
        checking_number()
        hard -= 1
    if hard == 0:
        print("You've run out of guesses, you lose. ")