# Game of BlackJack
from clear import clear
from Blackjack_Art import logo
import random as rd
import itertools
# Welcome message and c=game initiation
print(logo)
print("Welcome player!")
# Define the decks to use
number_of_decks = rd.randint(6,8)
suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
card_names = ['Ace', '2','3','4','5','6','7','8','9','10','Jack','Queen','King']
card_values = {
    'Ace': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
}

deck = list(itertools.product(card_names, suits))*number_of_decks

def choose_card():
    """Returns a random card from the deck of cards. The chosen card is removed from the deck"""
    card = deck.pop(rd.randint(0, len(deck)-1))
    return card

def total_card_value(card_deck):
    """Returns the total card value as the sum of cards in the card_deck. 
    If the deck contians one or more Aces and sum would be grater than 21, 
    then set Ace value to 1 by decreasing total by 10 until total would be less than 21."""
    total_value = 0
    num_aces = 0
    for card in card_deck:
        if card[0] == 'Ace':
            num_aces += 1  
        value = card_values[card[0]]
        total_value += value
    while total_value > 21 and num_aces > 0:
        total_value -= 10
        num_aces -=1
    return total_value

def blackjack():
    game_start = input("\nWould you like to play a game of Blackjack? Type 'y' or 'n'\n").lower()
    clear()
    if game_start == 'y':
        # Initial Player cards
        card_1 = choose_card()
        card_2 = choose_card()
        player_cards = [card_1, card_2]
        print(f"Your cards are: {player_cards}; Current Score: {total_card_value(player_cards)}")
        # Initial Computer cards
        comp_card_1 = choose_card()
        comp_card_2 = choose_card()
        computer_cards = [comp_card_1, comp_card_2]
        print(f"The Dealer's first card is: {comp_card_1}")
        # Computer decides if it wants to add card        
        deal_comp_cards = True
        comp_choices = ['y','n']
        while deal_comp_cards:
            add_comp_card = rd.choice(comp_choices)
            if add_comp_card == 'y':
                computer_cards.append(choose_card())
                computer_final_score = total_card_value(computer_cards)
            elif add_comp_card == 'n':
                deal_comp_cards = False
                computer_final_score = total_card_value(computer_cards)

        # Ask if player would like to draw a third card
        deal_player_cards = True
        if total_card_value(player_cards) == 21 and len(player_cards) == 2:
            print("You got a BlackJack. You Win!")
            deal_player_cards = False
        elif total_card_value(player_cards) == 21 and total_card_value(computer_cards) == 21 and len(player_cards) ==2 and len(computer_cards) == 2:
            print("Double BlackJack. This is a Super Rare Draw!!!")
            deal_player_cards = False
        while deal_player_cards:
            add_card = input("\nWould you like to draw another card? Type 'y' or 'n'\n").lower()
            clear()
            if add_card == 'y':
                player_cards.append(choose_card())
                print(f"Your cards are: {player_cards}; Current Score: {total_card_value(player_cards)}")
                print(f"Dealer's First Card: {comp_card_1}")
                player_final_score = total_card_value(player_cards)
                if player_final_score > 21:
                    break
            elif add_card == 'n':
                deal_player_cards = False
                print(player_cards)
                player_final_score = total_card_value(player_cards)
        clear()

        if player_final_score > 21:
            print(f"Your Cards: {player_cards}; Your Final Score: {player_final_score}")
            print(f"\nYou went over with a score of {player_final_score}. You Lose!")
        elif computer_final_score > 21 and player_final_score <= 21:
            print(f"Your Cards: {player_cards}; Your Final Score: {player_final_score}")
            print(f"\nDealer Cards: {computer_cards}; Dealer Final Score: {computer_final_score}")
            print(f"\nDealer went over with a score of {computer_final_score}. You Win with a score of {player_final_score}!")
        elif player_final_score == computer_final_score:
            print(f"Your Cards: {player_cards}; Your Final Score: {player_final_score}")
            print(f"\nDealer Cards: {computer_cards}; Dealer Final Score: {computer_final_score}")
            print(f"\nDealer and Player both scored {player_final_score}. This is a Draw!")
        elif player_final_score > computer_final_score:
            print(f"Your Cards: {player_cards}; Your Final Score: {player_final_score}")
            print(f"\nDealer Cards: {computer_cards}; Dealer Final Score: {computer_final_score}")
            print(f"\nYou scored higher than the dealer with a score of {player_final_score}. Dealer scored {computer_final_score}. You Win!")
        else:
            print(f"Your Cards: {player_cards}; Your Final Score: {player_final_score}")
            print(f"\nDealer Cards: {computer_cards}; Dealer Final Score")
            print(f"\nThe Dealer scored higher than you with a score of {computer_final_score}. You scored {player_final_score}. You Lose!")    
        
        blackjack()

    elif game_start == 'n':
        print("Goodbye!") 
    else:
        print("Invalid Input")   
        blackjack()  

blackjack()