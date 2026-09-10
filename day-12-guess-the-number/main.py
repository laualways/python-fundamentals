import random

from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

hard_or_easy = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if hard_or_easy == "hard":
    lives = 5
else:
    lives = 10

def game_started(lives_count):
    computer_choice = random.randint(1, 100)
    on_game = True

    while on_game:
        # print(computer_choice)
        attempt = int(input("Guess a number: "))

        if computer_choice == attempt:
            print(f"You got it! The answer was {computer_choice}!")
            on_game = False
        elif computer_choice > attempt:
            print("Too low.")
            lives_count -= 1
        elif computer_choice < attempt:
            print("Too high.")
            lives_count -= 1

        if lives_count == 0 and on_game:
            on_game = False
            print("You've run out of guesses. Refresh the page to run again.")
        elif on_game:
            print(f"You have {lives_count} attempts remaining to guess the number.\n")

game_started(lives)