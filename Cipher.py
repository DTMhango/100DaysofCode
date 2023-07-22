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
    print(f"The {direction}d message is '{message.capitalize()}'")

user_continue = True
while user_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction = direction, text = text, shift = shift)

    result = input("Type 'yes' if you would you like to go again. Otherwise type 'no.\n")
    if result == 'no':
        user_continue = False
        print('Thank you for using Caesar encryption. Goodbye!')