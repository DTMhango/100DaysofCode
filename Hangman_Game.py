# Hangman Game
from clear import clear
import random as rnd

word_list = ['burly',	'cabbage',	'noxious',	'wonderful',	'post',    'avoid',	'blood',	'outrageous',	'surprise',	'amuck',	'hop',	'guide',	'stitch',	'cars',	'key',	'rotten',	'seed',	'fasten',	'excellent',	'cagey',	'slave',	'point',	'embarrass',	'efficient',	'fool',	'leg',	'roasted',	'baby',	'apparel',	'ablaze',	'impulse',	'arrest',	'sail',	'eight',	'curve',	'intelligent',	'bushes',	'comb',	'black-and-white',	'glossy',	'drab',	'reign',	'race',	'drain',	'lovely',	'steel',	'cactus',	'alcoholic',	'learn',	'condition',	'clap',	'earthy',	'enter',	'comfortable',	'sophisticated',	'peck',	'develop',	'substance',	'therapeutic',	'utopian',	'ludicrous',	'harm',	'ship',	'like',	'mere',	'wrap',	'maid',	'snobbish',	'plot',	'standing',	'bouncy',	'pause',	'glass',	'cloudy',	'vessel',	'garrulous',	'nod',	'smoke',	'metal',	'magenta',	'aftermath',	'wacky',	'nine',	'broad',	'reflect',	'slow',	'bump',	'poised',	'jumpy',	'scared',	'available',	'signal',	'fence',	'festive',	'two',	'premium',	'thinkable',	'furniture',	'pen',	'calculating']
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''] 

# generate a random word
chosen_word = rnd.choice(word_list)
word_length = len(chosen_word)
# print(chosen_word)
blanks = '_'*word_length
display = []
display.extend(blanks)

# Ask user to guess a letter and assign it to a variable called 'guess'
lives = 6
end_of_game = False

from Logo import logo
print(logo)
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
        print(f"You already guessed {guess}")
    # Check if guess matches any letter in list of letters from chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # reduce number of lives for a wrong guess        
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You ran out of lives. You Lose! The correct word was '{chosen_word}'.")

    
    print(display)

    if '_' not in display:
        end_of_game = True
        print("Congratulations! You Win!")

    print(f"{' '.join(display)}")
    print(stages[lives])
  