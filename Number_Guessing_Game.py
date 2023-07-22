# Number 
from Guess_the_number_art import logo
from clear import clear
import random as rd

def checker():
    number = rd.randint(1,100)
    print(logo)
    lives_by_difficulty = {
        'easy': 10,
        'medium': 7,
        'hard': 5,
    }
    while True:
        print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
        difficulty = input("Choose a difficulty. Type 'easy', 'medium' or 'hard'\n").lower()
        if difficulty in lives_by_difficulty:
            lives = lives_by_difficulty[difficulty]
            break
        print("Invalid Input!")
        clear()
    
    while lives > 0:
        player_guess = int(input("Make a guess: "))        
        if player_guess == number:
            print(f"That's correct. You Win!. The number was {number}")
            if not continue_game():
                 return
        elif player_guess > number:
            print("Too high.\nGuess again.")
            lives -= 1
        elif player_guess < number:
            print("Too low.\nGuess again.")
            lives -= 1
        if lives == 0:
            print(f"Game Over! You Lose! The number was {number}")
            if not continue_game():
                 return

def continue_game():
    while True:
        play_again = input("Would you like to play again? Type 'y' or 'n'.").lower()
        if play_again == 'y':
            clear()
            checker()
            break
        elif play_again == 'n':
            clear()
            print("Goodbye!")
            return False
        else:
            print("Invalid Input!")

checker()

    