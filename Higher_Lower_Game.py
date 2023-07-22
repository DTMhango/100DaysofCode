from game_data import game_data
import random as rd
from clear import clear
from Higher_Lower_Art import logo, vs


def game_comp(celeb_a, celeb_b):
    print(logo)
    print(f"\nCompare A: {celeb_a['name']}, {celeb_a['description']}, {celeb_a['country']}, {celeb_a['follower_count']}")
    print(f"\n {vs}")
    print(f"\nAgainst B: {celeb_b['name']}, {celeb_b['description']}, {celeb_b['country']}")


def higher_lower():
    data = game_data[:]
    score = 0
    continue_game = True
    celeb_a = data.pop(rd.randint(0, len(data)-1))
    celeb_b = data.pop(rd.randint(0, len(data)-1))
    while continue_game:
        game_comp(celeb_a, celeb_b)
        user_guess = input("\nWho has more followers? Type 'A' or 'B':\n").capitalize()
        if user_guess not in ['A', 'B']:
            print("Invalid input, please try again")
            continue
        if celeb_a['follower_count'] >= celeb_b['follower_count'] and user_guess == "A" or celeb_a['follower_count'] < celeb_b['follower_count'] and user_guess == "B":
            score += 1
            clear()
            print(f"Correct! Current Score: {score}")
            celeb_a = celeb_b
            celeb_b = data.pop(rd.randint(0, len(data)-1))
            while celeb_b == celeb_a:
                celeb_b = data.pop(rd.randint(0, len(data)-1))
        else:
            print(f"Incorrect! You Lose! Your final score is: {score}")
            play_again = input("\nWould you like to play again? Type 'y' or 'n'\n")
            if play_again == "y":
                score = 0
                celeb_a = data.pop(rd.randint(0, len(data)-1))
                celeb_b = data.pop(rd.randint(0, len(data)-1))
                while celeb_b == celeb_a:
                    celeb_b = data.pop(rd.randint(0, len(data)-1))
                clear()
            else:
                continue_game = False


higher_lower()


