# Ceasar Cipher
from Caesar_Art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

def caesar(direction, text, shift):
    message = ''
    if direction == 'decode':
        shift = -shift
    for char in text:
        if char not in alphabet:
            new_char = char
        else:
            new_char = alphabet[(alphabet.index(char) + shift)%len(alphabet)]
        message += new_char
    print(f"\nThe {direction}d message is '{message.capitalize()}'\n")

def start():
    user_continue = True
    while user_continue:
        caesar(direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n\n")
               , text = input("Type your message:\n\n").lower(), shift = int(input("Type the shift number:\n\n"))) 
        
        result = input("Type 'yes' if you would you like to go again. Otherwise type 'no.\n\n")
        if result == 'no':
            user_continue = False
            print('\nThank you for using Caesar encryption. Goodbye!\n')

start()
