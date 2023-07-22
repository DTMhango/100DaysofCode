# Ceasar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction, text, shift):
    message = ''
    if direction == 'decode':
        shift = -shift
    for letter in text:
            new_letter = alphabet[(alphabet.index(letter) + shift)%len(alphabet)]
            message += new_letter
    print(f"The {direction}d message is '{message.capitalize()}'")

caesar(direction = direction, text = text, shift = shift)

# # Define encrypt function
# def encrypt(text, shift):
#     encoded_message = ''
#     for letter in text:
#         letter_num = alphabet.index(letter)
#         new_letter = alphabet[(letter_num + shift)%len(alphabet)]
#         encoded_message += new_letter
#     print(f"The encrypted message is '{encoded_message.title()}'")
# # Define decrypt function
# def decrypt(text, shift):
#     decoded_message = ''
#     for letter in text:
#         letter_num = alphabet.index(letter)
#         new_letter = alphabet[(letter_num - shift)%len(alphabet)]
#         decoded_message += new_letter
#     print(f"The decrypted message is '{decoded_message.title()}'")
      
# if direction == 'encode':
#       encrypt(text = text, shift = shift)
# elif direction == 'decode':
#       decrypt(text = text, shift = shift)


